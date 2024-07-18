import streamlit as st
import pandas as pd
import altair as alt 

st.title('点数表示')

st.write('あなたの点数を教えてください')

categories = ['国語', '数学', '社会', '理科','英語']

# スライダーで値を変更
values = [st.number_input(f'{cat}', min_value=0, max_value=100, value=10) for cat in categories]

# データフレームの作成
df = pd.DataFrame({'科目': categories, '点数': values})

# Streamlitのタイトル
st.title("科目と点数の棒グラフ")


# 棒グラフの作成
plt.bar(df['科目'], df['点数'], color='blue')
plt.xlabel('科目')
plt.ylabel('点数')
plt.title('科目ごとの点数')

# グラフの表示
st.pyplot(plt)




