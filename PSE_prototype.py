import streamlit as st
from PIL import Image
import random

def main():
    sel_list = {
        'Make a Schedule' : new_schedule,
        'My Plans' : myplans,
        'My Friends' : friend_trip,
        'Heatmaps' : heatmaps,
        'Notifications' : notifications

                }
    sel = st.sidebar.radio("", list(sel_list.keys()))
    sel_list[sel]()

def notifications():
    friend_list = ['Friend A', 'Friend B', 'Friend C', 'Friend D', 'Friend E']

    for idx, i in enumerate(friend_list):
        col = st.columns((1,1,1))
        col[0].write(f"{i} wants to join your trip (Trip {idx+1})")
        col[1].button("Accept", key=idx)
        col[2].button("Reject", key=idx)
        st.markdown('<hr>', unsafe_allow_html=True)


def heatmaps():
    st.text_input("Search")
    col = st.columns((1,3))
    col[0].write("Reported Activities")
    col[0].write("🟢 - Car Accidents")
    col[0].write("🟡 - Building on Fire")
    col[0].write("🔴 - Theft")
    col[1].image('heatmap.png')

    st.title("Numbers of Reports within the Area")
    st.write("Car Accidents - 12")
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write("Building on Fire - 2")
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write("Theft - 10")

def new_schedule():
    with st.form('schedule'):
        st.title("Google Maps API")
        location_list = ['Location A', 'Location B', 'Location C']
        st.image('map.jpg')
        d = st.text_input("Name This Trip")
        col1 = st.columns((1,1))
        col1[0].date_input("Date")
        col1[1].time_input("Time")

        col = st.columns((1,1,1))
        a = col[0].text_input('Location 1',location_list[0])
        b = col[1].text_input('Location 2',location_list[1])
        c = col[2].text_input('Location 3',location_list[2])


        submitted = col[0].form_submit_button('Add to plan')
        submitted1 = col[0].form_submit_button('Add to Favorites')
        submitted2 = col[0].form_submit_button('Clear')
        submitted3 = col[2].form_submit_button('Add a New Location')

def myplans():
    col = st.columns((1,1))
    col[0].write('My Plans')
    col[1].write('My favorites')

    for i in range(5):
        with col[0].expander(f'Trip {i+1}'):
            st.image('map.jpg')
            st.write(f'Location A → Location B → Location C')
            st.write('4/4/2022 - 10:00AM')
            st.button(f'Edit Trip {i+1}')
            st.button(f'Add Trip {i+1} to Favorites ')
            st.button(f'Delete Trip {i+1}')

            st.markdown('<hr>', unsafe_allow_html=True)
            st.title("Trip Safety: **92**%")
            st.write("1. Very few to no reports of any dangerous activity in the area")
            st.markdown('<hr>', unsafe_allow_html=True)

    with col[1].expander('To Work'):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')
        st.write('4/4/2022 - 08:00AM')
        st.button("Edit Trip ''To Work''")
        st.button("Delete Trip ''To Work''")
        st.button("Remove ''To Work'' from  Favorites")

        st.markdown('<hr>', unsafe_allow_html=True)
        st.title("Trip Safety: **62**%")
        st.write("1. There are some reports of theft in the area")
        st.write("2. Above average amount of covid cases reported in the area")
        st.markdown('<hr>', unsafe_allow_html=True)

    with col[1].expander('To School'):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')
        st.write('4/4/2022 - 08:00AM')
        st.button("Edit Trip ''To School''")
        st.button("Delete Trip ''To School''")
        st.button("Remove ''To School'' from  Favorites")
        st.write("Trip Safety: **92**%")

    with col[1].expander('Grocery Shopping'):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')
        st.write('4/4/2022 - 18:00PM')
        st.button("Edit Trip ''Grocery Shopping''")
        st.button("Delete Trip ''Grocery Shopping''")
        st.button("Remove ''Grocery Shopping'' from  Favorites")
        st.write("Trip Safety: **92**%")


def friend_trip():
    friend_list = ['Friend A', 'Friend B', 'Friend C', 'Friend D', 'Friend E']
    col = st.columns((1,1))
    col[0].write('Your Friends')
    col[1].write("Your Friends' Activities")

    radio_choice = col[0].radio('',friend_list)

    with col[1].expander(f"{radio_choice}'s Trip"):
        st.image('map.jpg')
        st.write(f'Location A → Location B → Location C')
        st.write('5/4/2022 - 9:00AM')
        st.markdown('<hr>', unsafe_allow_html=True)
        st.title("Trip Safety: **92**%")
        st.write("1. Very few to no reports of any dangerous activity in the area")
        st.markdown('<hr>', unsafe_allow_html=True)
        st.button(f"Join {radio_choice}'s Trip")


if __name__ == '__main__':
    main()
