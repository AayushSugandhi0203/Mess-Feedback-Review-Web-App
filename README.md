# Mess-Feedback-Review-Web-App
MESS FeedBack Review Web App

1) Dependencies:-
	a) django
	b) postgres
	c) psycopg2
	d) django-admin
	e)virtual enviorment
2) Setup and Run the Project:-
Activate the Virtual Environment using command mkvirtualenv (name_of_envionment)
Run the Project using command python manage.py runserver
Open the Link http://127.0.0.1:8000 on browser


3)Login and Register Page:-
	a) Login as Normal User:-
If you have already registered then enter your Registered Email Id and Password otherwise Register First. Then it will be directed to the Feedback Page.
	b) Login as Administration:- 
To Login as an admin fill Email field as "sugandhiaayush0203@gmail.com" and Password Field with "123456". Then it will be directed to the Admin Page.


 4) Feedback Page:-
	Student can submit their Mess Food Feedback for any meal by inserting date, type of meal and their name. Also, he can view the latest Mess Food Menu uploaded by the Mess Committee.


5) Administration Page:-
	Admin can upload the latest Mess Menu as decided by the Mess Committee as a pdf form. Admin can view the Feedback of the students along with the Sentiments classified in 5 formats from High Positive to High Negative.



6)Database:-
We have implemented the Database using PostgreSQL. We have used this Database because it comes with user-friendly GUI Feature named as Pgadminv4. PostgreSQL is a Relational Database, and it allows us the freedom to use, modify, and implement it as per our needs.

We have linked Database PostgreSQL and Backend using psycopg2.

7)Sentiment Analysis:-
We have developed two models ;
a) Binary Class Classification:- To classify whether the sentence is funny or not. To implement this, we have used Logistic Regression and attained an accuracy of 78%. 
b) Multiclass Classification:- To obtain the sentiments of the feedbacks. The model will classify the Sentiment into five classes viz High Positive, High Negative, Neutral, Negative, Positive. To implement this, we have used Logistic Regression as well as KNN and attained an accuracy of more than 70%.
Both model are trained stored into the pickle format.


8) Integration of Backend-Frontend-Database-ML Model:-
	Once the Feedback is submitted at the WebPage(Frontend), the data is collected by the Backend and feed into the Database. When the Feedback is accessed, first is fetched from the Database,and data is pushed into the Backend. The pickle file is loaded, and the ML Model
classifies the Sentiment and provides it to the Backend. Finally, the data from the Backend is passed, and it can be view on the WebPage(Frontend).

9) Model is Stored in 
messwebsite->mess->fun.py
messwebsite->mess->classify.py
messwebsite->mess->pickle_model.pkl
messwebsite->mess->pickle_model_classify.pkl

10) HTML files are stored in
messwebsite->mess->Templates
