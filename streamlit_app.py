import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

st.title('点数表示')

st.write('あなたの点数を教えてください')

number = st.number_input('国語', 50)
number = st.number_input('数学', 50)
number = st.number_input('社会', 50)
number = st.number_input('理科', 50)
number = st.number_input('英語', 50)

st.bar_chart(data=None, x=None, y=None, x_label=None, y_label=None, color=None, horizontal=False, width=None, height=None, use_container_width=True)


