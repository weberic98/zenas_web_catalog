import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

streamlit.header("Pick a sweatsuit color or style")
#Snowflake-related functions
def get_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from catalog_for_website")
        return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)


