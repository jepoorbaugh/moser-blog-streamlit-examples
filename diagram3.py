import streamlit as st

# Goal: show how updates inside fragment do not change the outside.
st.set_page_config("Diagram 3", layout="wide")
container = st.container()
with st.sidebar:
    with st.echo():
        with container:
            if "num_runs" not in st.session_state.keys():
                st.session_state.num_runs = 0

            if "num_frag_1_runs" not in st.session_state.keys():
                st.session_state.num_frag_1_runs = 0

            if "num_frag_2_runs" not in st.session_state.keys():
                st.session_state.num_frag_2_runs = 0

            @st.experimental_fragment()
            def fragment_1():
                st.session_state.num_frag_1_runs += 1
                with st.container(border=True):
                    st.header("Inside Fragment")

                    st.write(
                        f"Number of fragment 1 runs: {st.session_state.num_frag_1_runs}"
                    )

                    st.write(
                        f"Number of fragment 2 runs: {st.session_state.num_frag_2_runs}"
                    )

                    st.write(f"Number of page runs: {st.session_state.num_runs}")

                    st.button("Rerun fragment 1")

                    if st.button("Rerun page", key="inside_frag_1_btn"):
                        st.rerun()

            @st.experimental_fragment()
            def fragment_2():
                st.session_state.num_frag_2_runs += 1
                with st.container(border=True):
                    st.header("Inside Fragment 2")

                    st.write(
                        f"Number of fragment 1 runs: {st.session_state.num_frag_1_runs}"
                    )

                    st.write(
                        f"Number of fragment 2 runs: {st.session_state.num_frag_2_runs}"
                    )

                    st.write(f"Number of page runs: {st.session_state.num_runs}")

                    st.button("Rerun fragment 2")

                    if st.button("Rerun page", key="inside_frag_2_btn"):
                        st.rerun()

            st.session_state.num_runs += 1

            col1, col2 = st.columns(2)
            with col1:
                fragment_1()

            with col2:
                fragment_2()

            st.write(f"Number of page runs: {st.session_state.num_runs}")

            st.button("Rerun page", key="outside_frags_btn")
