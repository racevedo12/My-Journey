from django.urls import path
from .views import UserHomeView, PictureDetailView, AddPictureView, EditPictureView, DeletePictureView, LikePictureView, DislikePictureView, AddCommentView

urlpatterns = [
    # User Home Page
    path("", UserHomeView.as_view(), name="user_home_page"),

    # Picture Details
    path("picture/<int:pk>", PictureDetailView.as_view(), name="picture_detail"),

    # Adding a new picture
    path("picture/add", AddPictureView.as_view(), name="add_picture"),

    # Editing a picture
    path("picture/edit/<int:pk>", EditPictureView.as_view(), name="edit_picture"),

    # Deleting a picture
    path("picture/delete/<int:pk>", DeletePictureView.as_view(), name="delete_picture"),

    # Liking a picture
    path("picture/like/<int:pk>", LikePictureView, name="like_picture"),

    # Disliking a picture
    path("picture/dislike/<int:pk>", DislikePictureView, name="dislike_picture"),

    # Commenting a picture
    path("picture/comment/<int:pk>", AddCommentView.as_view() , name="comment_picture"),
]