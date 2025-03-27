import streamlit as st
# import langchain_helper as lp
import restaurant

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Select a Cuisine", ["Indian", "Italian", "Mexican", "Chinese", "Japanese", "Thai", "French", "American", "Greek", "Turkish", "Lebanese", "Korean", "Vietnamese", "Spanish", "British", "German", "Brazilian", "Portuguese", "Russian", "African", "Caribbean", "Middle Eastern", "Mediterranean", "Nordic", "Australian", "Canadian", "Latin American", "Other"])

if cuisine:
    response = restaurant.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
