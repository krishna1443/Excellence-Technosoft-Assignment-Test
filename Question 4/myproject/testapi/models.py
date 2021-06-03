from django.db import models

class Candidate(models.Model):
	name = models.CharField(max_length = 255, null = True)
	email = models.EmailField(null=True, unique=True, blank=True)
	address = models.CharField(max_length = 500, null = True)
	def __str___(self):
		return self.name +'--'+ self.email


class TestScore(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	TEST_NAME  = (
			("FIRST_ROUND","FIRST ROUND"),
			("SECOND_ROUND","SECOND ROUND"),
			("THIRD_ROUND","THIRD ROUND")
		)
	test_name = models.CharField(max_length=255, default="NO SELECTED", choices=TEST_NAME)
	score =  models.IntegerField(null=True, default=0)
	
	def __str___(self):
		return self.candidate.name +'--'+ self.test_name +'--'+ self.score



