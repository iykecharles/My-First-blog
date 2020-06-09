from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListview, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name="homepage"),
    path('blog/', PostListview.as_view(), name="blog-home"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('blog/create/', PostCreateView.as_view(), name="post-create"),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    

]
