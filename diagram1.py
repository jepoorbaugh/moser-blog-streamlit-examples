import streamlit as st

st.set_page_config("Diagram 1", layout="wide")

container = st.container()

with st.sidebar:
    with st.echo():
        with container:
            if "num_reloads" not in st.session_state.keys():
                st.session_state.num_reloads = 0
            else:
                st.session_state.num_reloads += 1

            st.title("My Streamlit app")
            st.write(f"Number of reloads: {st.session_state.num_reloads}")
            st.button("Click me!", type="primary")

            st.divider()

            user_name = st.text_input("Please write your name here")
            if not user_name == "":
                st.write(f"Welcome, **{user_name}**")
