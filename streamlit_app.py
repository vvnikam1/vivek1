import pandas as pd
import streamlit as st
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]}
df=pd.DataFrame(data)
st.table(df)






