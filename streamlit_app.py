import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('My parents New healthy diner')
streamlit.header(':bowl_with_spoon: Breakfast Menu')
streamlit.text(':green_salad: Omega 3 & Blueberry Oatmeal')
streamlit.text(':chicken: Kale, Spinach & Rocket Smoothie')
streamlit.text(':avocado::bread: Hard-Boiled Free-Range Egg')
streamlit.header(':banana::mango: Build Your Own Fruit Smoothie :kiwifruit::grapes:')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# write your own comment -what does the next line do?
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.text("The Fruit load list contains:")
# streamlit.text(my_data_row)
cmd=streamlit.text_input('custom query')
error=False
try:
    my_cur.execute(cmd)
except:
    error=True
if not error:
    streamlit.write(my_cur.fetchall())
else:
    streamlit.error('invalid query!!!')
