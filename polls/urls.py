from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [

   
   path('signup', views.signup, name='signup'),
   path('login', views.Login, name='login'),
   path('home', views.index, name='index'),
   path('<int:question_id>/', views.detail, name='detail'),
   path('<int:question_id>/results/', views.results, name='results'),
   path('<int:question_id>/vote/', views.vote, name='vote') 

]
