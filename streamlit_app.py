streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale Spinach and Rocket Smoothie')
streamlit.text('🐔 🥑🍞 Hard Boiled free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Load the initial fruit list from a CSV file
my_fruit_list = streamlit.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# User can pick fruits from the list
fruits_selected = streamlit.multiselect("Pick the fruit:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# User can enter a new fruit to add to the list
new_fruit = streamlit.text_input('Add a new fruit to the list:')

# Add the new fruit to the list if it is not empty
if new_fruit:
    my_fruit_list = my_fruit_list.append({'Carbs': 0, 'Protein': 0, 'Fat': 0}, ignore_index=True)
    my_fruit_list.index = my_fruit_list.index[:-1] + [new_fruit]

# Display the selected fruits and the new fruit added by the user
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# Fruityvice API response based on user input
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = streamlit.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

# Snowflake database connection and data retrieval
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains")
streamlit.dataframe(my_data_rows)


# import streamlit
# streamlit.title('My parents new healthy diner')
# streamlit.header('Breakfast Menu')
# streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
# streamlit.text('🥗 Kale Spinach and Rocket Smoothie')
# streamlit.text('🐔 🥑🍞Hard Boiled free Range Egg')
# streamlit.text('🥑🍞Avocadp Toast')

# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')
# # Let's put a pick list here so they can pick the fruit they want to include 
# # putting a pick list of the fruits for the customer.
# fruits_selected = streamlit.multiselect("Pick the fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
# # Display the table on the page.

# streamlit.dataframe(fruits_to_show)
# # new section to display fruityvice api response
# streamlit.header("Fruityvice Fruit Advice!")
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)


# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# # normalizing the json response
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# streamlit.dataframe(fruityvice_normalized)


# import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit load list contains")
# streamlit.dataframe(my_data_rows)

# f_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', f_choice)


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)



                                        

