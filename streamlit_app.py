import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_to_show = my_fruit_list.loc[fruits_selected]



streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
  streamlit.error()  
  



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to have?')
streamlit.write('The user entered', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

streamlit.stop()




