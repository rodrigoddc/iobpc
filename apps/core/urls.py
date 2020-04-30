from django.urls import path
from apps.core.views.index_view import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
