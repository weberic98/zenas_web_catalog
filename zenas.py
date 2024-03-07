import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

#streamlit.header("Pick a sweatsuit color or style")
#Snowflake-related functions
def get_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from catalog_for_website")
        return my_cur.fetchall()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_load_list()
my_cnx.close()
streamlit.dataframe(my_data_rows)

my_clothing_list = my_data_rows

# Let's put a pick list here so they can pick the fruit they want to include 
clothing_selected = streamlit.selectbox("Pick some clothing:", list(my_data_rows))
clothing_to_show = my_clothing_list.loc[clothing_selected]

