from django.urls import path
from .views import PostView, PostDetail, AddComment, AddLike, DeleteLike

urlpatterns = [
    path('', PostView.as_view(), name='post-view'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('review/<int:pk>', AddComment.as_view(), name='add_comment'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('<int:pk>/add_like', AddLike.as_view(), name='add-like'),
    path('<int:pk>/del_like', DeleteLike.as_view(), name='del-like'),
]