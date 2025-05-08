# victory_day.py
import streamlit as st

st.set_page_config(page_title="День Победы", page_icon="🎖", layout="centered")

st.title("🎖 С Днём Победы!")
st.subheader("9 Мая — День великой Победы!")

st.markdown(
    """
    Спасибо за мужество, за стойкость и за мир!

    🕊️ **Мы помним. Мы гордимся.**
    """
)

st.image("victory.jpg", caption="С Праздником Великой Победы!")

st.write("Создано с любовью ❤️ в честь 9 Мая")

