import streamlit as st

def display_subject_area(title, description_dict):
    st.subheader(title)
    cols = st.columns(len(description_dict))
    for i, (area, desc) in enumerate(description_dict.items()):
        with cols[i]:
            st.markdown(f"### {area}", unsafe_allow_html=True)
            st.write(desc)
