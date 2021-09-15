from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    # ex: /polls/deepthoughts
    path('deepthoughts', views.ThoughtView.as_view(), name='thought'),
    # ex: /polls/deepthoughts/list

    path('add', views.add, name='add'),

    path('deepthoughts/list', views.ListView.as_view(), name='list'),

]