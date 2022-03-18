import streamlit as st
from PIL import Image
import random

def main():
    sel_list = {
        'Make a Schedule' : new_schedule,
        'My Plans' : myplans,
        'Your Friends' : friend_trip,

                }
    sel = st.sidebar.radio("", list(sel_list.keys()))
    sel_list[sel]()

def new_schedule():
    with st.form('schedule'):
        st.title("Google Maps API")
        location_list = ['Location A', 'Location B', 'Location C']
        st.image('map.jpg')
        d = st.text_input("Name This Trip")
        col = st.columns((1,1,1))
        a = col[0].text_input('Location 1',location_list[0])
        b = col[1].text_input('Location 2',location_list[1])
        c = col[2].text_input('Location 3',location_list[2])

        submitted = col[0].form_submit_button('Confirm')
        submitted1 = col[0].form_submit_button('Clear')
        submitted2 = col[2].form_submit_button('Add a New Location')

def myplans():
    col = st.columns((1,1))
    col[0].write('My Plans')
    col[1].write('My favorites')

    for i in range(5):
        with col[0].expander(f'Trip {i+1}'):
            st.image('map.jpg')
            st.write(f'Location A → Location B → Location C')

    with col[1].expander('To Work'):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')

    with col[1].expander('To School'):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')

    with col[1].expander('Grocery Shopping'):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')


def friend_trip():
    friend_list = ['Friend A', 'Friend B', 'Friend C', 'Friend D', 'Friend E']
    col = st.columns((1,1))
    col[0].write('Your Friends')
    col[1].write("Your Friends' Activities")

    radio_choice = col[0].radio('',friend_list)

    with col[1].expander(f"{radio_choice}'s Trip"):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')
        st.button(f"Join {radio_choice}'s Trip")


if __name__ == '__main__':
    main()
