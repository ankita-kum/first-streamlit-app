import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourite')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spanich & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#streamlit.text('🍌 Banana Smoothie')
#streamlit.text('🥭 Mango Smoothie')
#streamlit.text('🥝 Kiwi Smoothie')
#streamlit.text('🍇 Grapes Smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
