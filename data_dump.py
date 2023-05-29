import pymongo
import pandas as pd
import json

#Dumping the data in MongoDB with below code

#provide mongoDb localhost URL to connect python to MongoDb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and Columns', {df.shape})

    #So this is CSV record let's convert this dataset into JSON because MongoDB takes only JSON data.
    df.reset_index(drop=True, inplace=True)

    #This code will convert CSV dataset into JSON format
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Below code will insert converted JSON into MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)