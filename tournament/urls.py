from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('', views.index, name='tournament_index'),
    path('add/', views.add, name='tournament_add'),
    path('edit/<slug:id>/', views.edit, name='tournament_edit'),
    path('timer/', views.timer, name='timer'),
    path('<slug:id>/', views.view, name='tournament_view'),
    path('add/participant/<slug:id>/', views.participant_add, name='tournament_participant_add'),
    path('update/<slug:id_t>/<slug:id>/', views.participant_update, name='tournament_participant_update'),
    path('participant/edit/', views.participant_edit, name='tournament_participant_edit'),
    
    path('<slug:id>/add/matches/', views.tournament_matchs_add, name='tournament_matchs_add'),
    path('<slug:id>/add/matches/<slug:id_p1>/', views.tournament_matchs_add, name='tournament_matchs_add'),
    path('<slug:id>/add/matches/<slug:id_p1>/<slug:id_p2>/', views.tournament_matchs_add, name='tournament_matchs_add_load_deck'),

    path('start_challonge/<slug:id>/',view=views.start_challonge,name='tournament_start_challonge'),
    path('<slug:id>/<slug:participant>/', view=views.participant_view, name='tournament_participant_view'),

]