from django.urls import path
from . import views
urlpatterns = [
    # localhost8000/posts/
    path('', views.dashboard),
    # localhost:8000/posts/<post_id>/delete
    path('<int:post_id>/delete', views.delete),
    path('post_message', views.post_mess),
    path('add_comment/<int:id>', views.post_comment),
    path('delete/<int:id>', views.delete_comment),

]
