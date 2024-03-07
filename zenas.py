import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the dafta into a dataframe 
df = pandas.DataFrame(my_catalog)

# put the first column into a list 
color_list = df[0].values.tolist()

# Let's put a pick list here so they can pick the clothing they want
clothing_selected = streamlit.selectbox("Pick some clothing:", list(color_list))


