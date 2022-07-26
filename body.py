import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# PASSWORD CHECKER
Are you cofident  that your password is **STRONG** or not?
""")

def pw_check(password):
   
    point = 0
    num = False
    upper = False
    lower = False
    alphanum = False

    for letter in password:
        if letter.isnumeric():
            num = True
        elif letter.islower():
            lower = True
        elif letter.isupper():
            upper = True
        elif not letter.isalnum():
            alphanum = True
        if upper and lower and num and alphanum:
            break
    if lower == True:
      point+=5
    if lower == True and upper == True:
      point+=10
    if lower == True and num == True:
      point+=10
    if lower == True and alphanum == True:
      point+=10
    if len(password) >= 8:
      point+=5
      
      return point

pw = st.text_input('Enter your password', '#HireMe1234')
pwd = pw_check(pw)
st.subheader('Your Point')
st.write(pwd)
st.write("Good" if pwd >= 35 else "Bad")
if upper != True:
   st.warning('The password need at least 1 uppercase letter.')
elif num != True:
   st.warning('The password need at least 1 number.')
elif alphanum != True:
   st.warning('The password need at least 1 uppercase letter.')
elif len(pw)<8:
   st.warning('The password need to be at least 8 characters.')

    
    

