from django.conf.urls import patterns, include, url

from . import views
from . import auth

app_name = 'coderunner'
urlpatterns = [
    path('', views.main, name='mainView'),
    path('problems', views.allProblems, name='allProblemsView'),
    path('problems/([A-Z]+)', views.problemDetail, name='problemDetailView'),
    path('problems/judge/([A-Z]+)', views.judgeProblem, name='judgeView'),
    path('submissions', views.submissions, name='submissionsView'),
    path('account', views.account, name='accountView'),

    path('logout', auth.logout_view, name='logoutView'),
    path('login', auth.login_view, name='loginView'),
    path('signup', auth.signup_view, name='signupView'),
]