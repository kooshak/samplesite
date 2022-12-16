from django.urls import path

from .views import index, marks, subjects, notebook, login

urlpatterns = [
    path('home/', index, name='index'),
    path('marks/', marks, name='marks'),
    path('subjects/', subjects, name='subjects'),
    path('notebook/', notebook, name='notebook'),
    path('', login, name='login'),
    ]