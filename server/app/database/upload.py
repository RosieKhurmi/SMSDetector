# Upload CSV to database

import pandas as pd
from models import insert_data
from connections import list_collection


# Extract information from csv_dictionary and return contents
def extract_csv_info(csv_info):
    csv_file = csv_info['path']
    type_col = csv_info['type']
    content_col = csv_info['content']
    spam_name = csv_info['spam']
    ham_name = csv_info['ham']

    return csv_file, type_col, content_col, spam_name, ham_name


# Sort spam and ham from the dictionary and return spam dataframe and ham dataframe
def sort_spam_ham(csv_info):
    csv_file, type_col, content_col, spam_name, ham_name = extract_csv_info(csv_info)

    df = pd.read_csv(csv_file)
    df = df.rename(columns={type_col: 'Type', content_col: 'Content'})

    spam_df = df[df['Type'] == spam_name]
    ham_df = df[df['Type'] == ham_name]

    return spam_df, ham_df


# Insert both dataframes to mongoDB
def insert_spam_ham(csv_info):
    spam_df, ham_df = sort_spam_ham(csv_info)
    collections = list_collection()

    insert_data(spam_df, collections[0])
    insert_data(ham_df, collections[1])


# Dictionary: Will later be converted into a JSON that can be loaded in
csv_info = [
    {
        'path': 'data/sms.csv',
        'type': 'v',
        'content': 'v2',
        'spam': 'spam',
        'ham': 'ham'
    },
]

# Call the function
insert_spam_ham(csv_info[0])
