import streamlit as st
import csv
import pandas as pd
import plotly.express as px
import numpy as np


st.title("Injustice anywhere is a threat to justice everywhere")


st.markdown('“The chief problem in any community cursed with crime is not Punishment of the criminals, but the preventing of the young from being trained to crime.For our society to be better, we must revive our conscience and do Godly things."')


    





#crime = pd.read_csv("model.csv")

 #data = st.file_uploader("Upload your csv file", type=["csv"])
#if data is not None:
#df = pd.read_csv(data)
#st.dataframe(df.head())
#df = st.cache(pd.read_csv)("model.csv")
#After reading the csv file, visualise the dataframe with the below code:
is_check = st.checkbox("Display Analysed Data")
#if is_check:
 #st.write(df)
#variables = st.sidebar.multiselect("Enter the variables", df.columns)
#st.write("You selected these variables", variables)


if is_check:
    print('crime rate')
    with open("model.csv", "r") as csv_file:
     reader = csv.DictReader(csv_file)
     total_type1 = sum(float(row["Murder"]) for row in reader)
    print(total_type1)
    with open("model.csv", "r") as csv_file:
      reader = csv.DictReader(csv_file)
      total_type2 = sum(float(row["Chain Snatching"]) for row in reader)
    print(total_type2)
    with open("model.csv", "r") as csv_file:
      reader = csv.DictReader(csv_file)
      total_type3 = sum(float(row["Rape"]) for row in reader)
    print(total_type3)

    random_x = [total_type1,total_type2,total_type3]
    names = ['crime','science','computer'] 
  
    fig = px.pie(values=random_x, names=names,title='Crime Rate',color_discrete_sequence=px.colors.sequential.RdBu) 
    fig.show()
