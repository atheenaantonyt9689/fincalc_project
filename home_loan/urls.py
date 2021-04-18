from django.urls import path 
from .views import HomeLoanView


urlpatterns = [
path('homeloan',HomeLoanView.as_view()),
#path('', HomePageView.as_view(), name='home'),
]
