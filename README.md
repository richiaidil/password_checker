# password_checker web app
This web app provide a simple point system to evaluate the strength of user input password.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Next improvement](#next-improvement)

## General info
This web app can evaluate user input password by deploying a simple point system. The system will mark the password is 'Good" if the point is more than 35. The parameter for the system is the password has lowercase letter, uppercase letter, number, any punctuation mark and length of the password itself. It also will tell what the improvement that user can made to increase the strength of password.

The project is actually an unguided project from datacamp (link): a project to determine the percentage of 'Good' password in a set of user email and password. I decided to deploy the code into web app as my portfolio and introduce a simple point and feedback system just to make it fun.
	
## Technologies
Project is created using Python 3.9 with following packages:
* Numpy
* Pandas
* streamlit.io

## Next improvement
There is other step or features can be added to the web app to increase its functioanlity:
* Deploy a visual indicator for the points (maybe a strength bar with green colout for 'Good' and red colour for 'Bad')
* A random password generator or seed phrase
