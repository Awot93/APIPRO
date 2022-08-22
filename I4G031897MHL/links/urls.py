from django.urls import path
#from . import views
from .views import PostListApi, PostCreateApi, PostDetailApi, PostUpdateApi, PostDeleteApi 
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet


router = DefaultRouter()

router.register(r'Link=', LinkViewSet, basename='link')


app_name="link"
'''
urlpatterns = [
    path("create/", PostCreateApi.as_view({'get': 'list'}), name="api_create"),
    path("update/<int:pk>", PostUpdateApi.as_view({'get': 'list'}), name="api_update"),
    path("delete/<int:pk>", PostDeleteApi.as_view({'get': 'list'}), name="api_delete"),
    path("", PostListApi.as_view({'get': 'list'}), name="api_list"),
]
'''

urlpatterns = [] + router.urls
