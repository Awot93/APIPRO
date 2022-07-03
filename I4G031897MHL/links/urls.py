from django.urls import path
#from . import views
from .views import PostListApi, PostCreateApi, PostDetailApi, PostUpdateApi, PostDeleteApi 

app_name="link"

urlpatterns = [
    path("create/", PostCreateApi.as_view({'get': 'list'}), name="api_create"),
    path("update/<int:pk>", PostUpdateApi.as_view({'get': 'list'}), name="api_update"),
    path("delete/<int:pk>", PostDeleteApi.as_view({'get': 'list'}), name="api_delete"),
    path("", PostListApi.as_view({'get': 'list'}), name="api_list"),
]