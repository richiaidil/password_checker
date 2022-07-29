import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# PASSWORD CHECKER
Are you cofident  that your password is **STRONG** or not?
""")

def pw_check():
   
    pw = st.text_input('Enter your password', '#HireMe1234')
    point = 0
    num = False
    upper = False
    lower = False
    alphanum = False
    min_length = False

    for letter in pw:
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
    if len(pw) >= 8:
      point+=15
      min_length = True
    
    if lower != True:
       st.warning('Your password need to has at least 1 lowercase letter.')
    if upper != True:
       st.warning('Your password need to has at least 1 uppercase letter.')
    if num != True:
       st.warning('Your password need to has at least 1 number.')
    if alphanum != True:
       st.warning('Your password need to has at least 1 punctuation mark.')
    if min_length != True:
       st.warning('Your password need to be at least 8 characters.')
 
    return point

pt = pw_check()

st.subheader('Your Point')
st.write(pt)
st.write("Good" if pt >= 35 else "Bad")



    
    

