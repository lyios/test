import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

st.title('点数表示')

st.write('あなたの点数を教えてください')

number = st.number_input('国語', 0)
number = st.number_input('数学', 0)
number = st.number_input('社会', 0)
number = st.number_input('理科', 0)
number = st.number_input('英語', 0)


