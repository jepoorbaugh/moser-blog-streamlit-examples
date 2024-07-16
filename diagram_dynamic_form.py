import streamlit as st
import streamlit as st

st.set_page_config("Diagram 1")

tab1, tab2 = st.tabs(["Default", "Goal"])

with tab1:
    st.title("Write Review")
    with st.form(border=True, key="rating_form"):
        st.text_input("Username", key="form_name")
        st.slider("Rating", 0.5, 5.0, step=0.5, key="form_rating")
        st.text_area("Comment (Required if rating <= 2.5)", key="form_comment")

        st.form_submit_button("Submit", type="primary")

    if len(st.session_state.form_comment) == 0 and st.session_state.form_rating <= 2.5:
        st.error("Please enter a comment for ratings <= 2.5")
    elif st.session_state.form_name == "":
        st.error("Please enter your name")
    else:
        if not len(st.session_state.form_name) == 0:
            st.success(f"Thank you, {st.session_state.form_name} for your feedback!")

with tab2:
    st.title("Write Review")

    @st.experimental_fragment()
    def dynamic_form():
        with st.container(border=True):
            st.text_input("Username", key="frag_name")
            st.slider("Rating", 0.5, 5.0, step=0.5, key="frag_rating")
            st.text_area("Comment (Required if rating <= 2.5)", key="frag_comment")

            is_invalid = (
                len(st.session_state.frag_comment) == 0
                and st.session_state.frag_rating <= 2.5
            ) or st.session_state.frag_name == ""
            if st.button(
                "Submit",
                type="primary",
                disabled=is_invalid,
            ):
                st.rerun()

    dynamic_form()
    if not len(st.session_state.frag_name) == 0:
        st.success(f"Thank you, {st.session_state.frag_name} for your feedback!")


# container = st.container()
# # Goal: show the best form we can make w.o fragments
# with st.sidebar:
#     with st.echo():
#         with container:
