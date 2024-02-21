from django.urls import path
from .views import BrewList, BrewDetail

urlpatterns = [
  path("", BrewList.as_view(), name="brew_list"),
  path("<int:pk>/", BrewDetail.as_view(), name="brew_detail"),
]