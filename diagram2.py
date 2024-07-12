import streamlit as st
import random

st.set_page_config("Diagram 2", layout="wide")

container = st.container()
with st.sidebar:
    with st.echo("above"):
        with container:
            # Define our session state variable
            if "user_name" not in st.session_state.keys():
                st.session_state.user_name = ""

            # Program starts executing here
            st.header("My Streamlit App")

            # Write out the current value of our session state variable.
            st.write(f"User name: {st.session_state.user_name}")

            # Change the value of the session state variable
            # When this widget is updated, the page will rerun from the top.
            # However, the session state variable will only be updated when Streamlit renders this widget
            # which means that the value of this variable will only be updated after it has been used above.
            st.session_state.user_name = st.text_input("Please type your name")
