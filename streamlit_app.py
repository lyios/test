import streamlit as st
import pandas as pd
import altair as alt 
import matplotlib.pyplot as plt

st.title('点数表示')

st.write('あなたの点数を教えてください')

number = st.number_input('国語', 50)
number = st.number_input('数学', 50)
number = st.number_input('社会', 50)
number = st.number_input('理科', 50)
number = st.number_input('英語', 50)

data = {
    '科目': ['国語', '数学', '社会', '理科','英語'],
    '点数': [10, 15, 7, 20]
}
df = pd.DataFrame(data)

# Streamlitのタイトル
st.title("カスタマイズされた棒グラフの例")

# 棒グラフの作成
plt.bar(df['科目'], df['点数'], color='blue')
plt.xlabel('科目')
plt.ylabel('点数')
plt.title('科目ごとの点数')

# グラフの表示
st.pyplot(plt)




