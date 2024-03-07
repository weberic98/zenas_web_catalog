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

clothing_selected = streamlit.multiselect("Pick a sweatsuit color or style:", list(get_load_list.index))
clothing_to_show = my_clothing_list.loc[clothing_selected]



