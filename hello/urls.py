from django.urls import path
from . import views
app_name = "hello"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("arantxa", views.arantxa, name="arantxa"),
    path("david", views.david, name="david")
]
