import pandas as pd
from connections import get_collection

# Insert data to MongoDB
'''
@param: dataframe, collection_name
'''
def insert_data(df, collection_name):
    collection = get_collection(collection_name)
    records = df.to_dict(orient='records')
    collection.insert_many(records)


# Load data from MongoDB
'''
@param: collection_name
'''
def load_data(collection_name):
    collection = get_collection(collection_name)
    data = pd.DataFrame(list(collection.find()))
    return data
