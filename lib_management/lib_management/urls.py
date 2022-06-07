from django.contrib import admin
from django.urls import include, path

from library.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('book/add', BookAdd),
    path('bookEdit/<int:id_b>', BookEdit),
    path('bookEdit/bookUpdate',BookUpdate),
    path('bookDetail/',BookDetail),
    path('login/',Login),
    path('admin/',admin_home),
    path('bookInfo/<int:id_b>',bookInformation),
    path('admin-collections',ADcollections),
    path('search-book',searchBook),

]