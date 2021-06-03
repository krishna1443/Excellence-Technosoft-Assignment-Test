from django.contrib import admin
from .models import Candidate, TestScore

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'email','address']

@admin.register(TestScore)
class TestScoreAdmin(admin.ModelAdmin):
	list_display = ['id', 'candidate', 'test_name', 'score']


