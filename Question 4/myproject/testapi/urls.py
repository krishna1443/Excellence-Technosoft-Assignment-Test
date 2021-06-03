from django.urls import path
from . import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI



urlpatterns = [
    path('candidates/', views.candidates, name = 'candidates'),
    path('candidate_update/<int:pk>', views.candidate_update, name = 'candidate_update'),
    path('testscores/', views.testscores, name = 'testscores'),
    path('highscores/', views.highscores, name = 'highscores'),
    path('averagescores/', views.averagescores, name = 'averagescores'),

    path('register/', RegisterAPI.as_view(), name='register'),

    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
     
]


