import streamlit as st
import pandas as pd

df = pd.read_csv('test.csv')

st.subheader("Данные")
st.dataframe(df)
 
if st.checkbox("Показать статистику"):
   st.subheader("Статистика")
   st.write(df.describe())

column = st.selectbox("Выберите столбец", df.columns)
st.line_chart(df[column])

st.subheader("Фильтрация данных")
unique_values = st.multiselect("Выберите уникальные значения", df[column].unique())
filtered_data = df[df[column].isin(unique_values)]
st.dataframe(filtered_data)

if st.checkbox("Использовать слайдер для выбора числа строк"):
	num_rows = st.slider("Выберите количество отображаемых строк", 1, len(df), 5)
	st.dataframe(df.head(num_rows))

st.subheader("Гистограмма столбца")
histogram_column = st.selectbox("Выберите столбец для гистограммы", df.columns)
st.bar_chart(df[histogram_column].value_counts())
