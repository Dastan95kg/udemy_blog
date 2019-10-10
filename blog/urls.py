from django.urls import path
from .views import (AboutView, PostListView, 
                    PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, 
                    DraftListView, add_comment_to_post,
                    comment_approve, comment_remove,
                    post_publish)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('<int:pk>/publish/', post_publish, name='post_publish')
]