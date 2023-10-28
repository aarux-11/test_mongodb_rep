import streamlit as st
import pymongo

import pandas as pd

#Bridging a connection with MongoDB Atlas and Creating a new database(youtube_data)
client = pymongo.MongoClient("mongodb+srv://Aarushi:'%40%40rushi1108'@youtubeproject.nrit3zy.mongodb.net/?retryWrites=true&w=majority")
db = client.youtube_data

st.write("Here's our first attempt at using data to create a table:")
data = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

st.table(data)

if st.button("Upload to MongoDB"):
    with st.spinner('Please Wait for it...'):
        collections1 = db.data_details
        collections1.insert_many(pd.DataFrame(data, columns=list('first_column')))
