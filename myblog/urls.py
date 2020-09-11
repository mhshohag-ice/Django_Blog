from django.urls import path
#from . import views
from .views import IndexView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    #path('', views.index, name="index"),
    path('', IndexView.as_view(), name="index"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),

]