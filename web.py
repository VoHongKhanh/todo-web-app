# pip install streamlit
''' https : // khanhvohong-todo-web-app . streamlit . app / '''
import streamlit as st
from modules.my_lib import *

#if 'txt_todo' not in st.session_state:
#    st.session_state.txt_todo = ""


def add_todo():
    global todos
    todo = st.session_state.txt_todo
    if not (todo in todos):
        todos += [todo]
        write_data(todos)
    st.session_state.txt_todo = ""


def add_complete(index):
    global todos, mission_completed
    todo = todos[index]
    mission_completed += [todo]
    write_data(mission_completed, missionCompletedFile)

    todos.pop(index)
    write_data(todos)


def remove_complete(index):
    global mission_completed
    mission_completed.pop(index)
    write_data(mission_completed, missionCompletedFile)


todos = read_data()
mission_completed = read_data(missionCompletedFile)

st.set_page_config(layout="wide")

st.title("My Todo Web Application")
st.subheader("This is my todo web application")
st.write("<a href='mailto:khanhvh.fpt@gmail.com'>khanhvh.fpt@gmail.com</a> # <a href='tel:0976755191'>0976 755 191</a>", unsafe_allow_html=True)

st.text_input(label="", placeholder="Enter your todo here and then press Enter to add new todo", key="txt_todo", on_change=add_todo)

if len(todos)==0:
    st.write("You don't have any to do.<br/>Please enter new todo into the textbox below and then press Enter to add new todo!")
else:
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("To do list")
    for index, todo in enumerate(todos):
        chk_todo = st.checkbox(todo, key=f"todo{index}")
        if chk_todo:
            add_complete(index)
            del st.session_state[f"todo{index}"]
            st.experimental_rerun()

if len(mission_completed)>0:
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("Completed mission")
    for index, todo in enumerate(mission_completed):
        chk_complete = st.checkbox(todo, key=f"complete{index}")
        if chk_complete:
            remove_complete(index)
            del st.session_state[f"complete{index}"]
            st.experimental_rerun()