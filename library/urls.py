from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    #path('<int:book_id>/edit_book',views.index,name='index'),
]