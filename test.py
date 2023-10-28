import streamlit as st
import pymongo

import pandas as pd

#Bridging a connection with MongoDB Atlas and Creating a new database(youtube_data)
# client = pymongo.MongoClient("mongodb+srv://Aarushi:'%40%40rushi1108'@youtubeproject.nrit3zy.mongodb.net/?retryWrites=true&w=majority")
# db = client.YT_DataFetch

from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://Aarushi:education11@youtubeproject.nrit3zy.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING, tlsAllowInvalidCertificates=True)
    
    return client['YT_DataFetch']

if __name__ == "__main__":
    dbname = get_database()

dbname = get_database()
collection_name = dbname["channel_details"]

st.write("Here's our first attempt at using data to create a table:")

data = [["Channel_Name", "Example Channel"],["Channel_Id", "UC1234567890",]]

data = pd.DataFrame(data, columns=['Channel','Details'])

st.table(data)

if st.button("Upload to MongoDB"):
    with st.spinner('Please Wait for it...'):
        collection_name.insert_many(data.to_dict('records'))
        st.success("Upload to MogoDB successful !!")
