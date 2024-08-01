from django.urls import path
from . import views


# app_name = 'events'
urlpatterns = [
    path('events/', views.EventsListView.as_view(), name='events'),
    path('events/<int:pk>/', views.EventsDetailView.as_view(), name='event-detail'),# Add a URL pattern for retrieving a specific event by its ID
    path('users/', views.CustomUserCreateView.as_view(), name='users'),
]

