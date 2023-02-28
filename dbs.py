import mysql.connector
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})
cnx = mysql.connector.connect(user='root', password='mysqlinstaller@001',
                              host='localhost', database='bi',port='3305')
st.write(cnx)


# Read data from the database into a dataframe
st.header("EDA Application 🌐")
data = pd.read_sql('SELECT * FROM entry', con=cnx)



# Display the dataframe in your Streamlit app
st.info("Dataset.............")
st.dataframe(data)

st.sidebar.header("Student Details 🔥")


#showing top 5 data from dataset
h1=data.head()
st.sidebar.warning('TOP 5 Data')
st.sidebar.write(h1)
h2=data.tail()
st.sidebar.error('Bottom 5 Data')
st.sidebar.write(h2)




fig=plt.figure(figsize=(10,5))
st.subheader("Student's Marks Bar Chart")
plt.xticks(rotation=60)
bar=sns.barplot(x='fname',y='marks',palette='viridis',data=data)
for p in bar.patches:
    bar.annotate(format(p.get_height(), '.2f'),
                   (p.get_x() + p.get_width() / 2,
                    p.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
st.pyplot(fig)



fig=plt.figure(figsize=(10,5))
st.sidebar.subheader('Department counts :')
branch=data['dept'].value_counts()
st.sidebar.write(branch)