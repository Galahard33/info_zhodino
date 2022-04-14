from django.urls import path

from . import views


# Register your urls here

urlpatterns = [path("", views.simple_view)]

# To register this URLS
# path("test_app/", include("apps.test_app.web.urls"))
