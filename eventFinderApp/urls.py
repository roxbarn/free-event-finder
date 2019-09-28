from django.urls import path
from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # path('account/', views.AccountView.as_view(), name='account'),
    path('account/', views.account, name='account'),
    # event-finder/addevent
    path('addeventcreateview/', views.AddEventCreateView.as_view(), name='addevent'),
    path('<int:pk>/event_edit/', views.EditEvent.as_view(), name='editevent'),
    
]

