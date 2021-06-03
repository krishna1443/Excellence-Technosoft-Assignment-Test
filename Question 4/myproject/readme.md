[Note:* Before this, must installed djangorestapi]
1.create django project and app
2.create models.py inside app
 - create class Candidate
 	- cid : autoincreament
 	- name : CharField
 	- email : EmailField

 - create class TestScore
 	 - tid : autoincreament
 	 - cid : Fk
 	 - test_name : SelectField (first_round, second_round, third_round)
 	 - score : SelectField (till 10)

3.create a serializers.py for rest api
	- import models classes
	- create CandidateSerializer
		- define fields of Candidate model
	- create TestScoreSerializer
		- define fields of TestScore model

4.now create the function for restapi in views.py
	- create function 'candidate'
		- if request.method is POST so add data to database
	- create 'testscores' function
	 	- if request.method is post, so add assign score of the candidate in TestScore model
	- create 'highscores' function
		- if request.method is GET so return high scoring candidate data
	- create 'averagescores' function
		- if request.method is GET so return first_round, second_round, third_round
		calculate average score as per all three round and return

5.create urls.py
	candidates/ post insert candidate data
    testscores/ post insert test score data
    highscores/ get  show high score candidate name
    averagescores/ get show average score by test name
		 

6.check the admin panel
-create super user
http://127.0.0.1:8000/admin/

Now, check all with postman

