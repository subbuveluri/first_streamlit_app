import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast favorites')

streamlit.text('omega 3 & blueberry oatmeal')

streamlit.text('kale, spinach & rocket smoothie')

streamlit.text('Hard-boiled free-range egg')

streamlit.text('Avocado Toast')

streamlit.header('Bulid your own fruit smoothie')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

#take the json version of the responds and normalized it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
