from django.urls import path
from .views import UserView
urlpatterns = [
    path("users/", UserView.as_view({'get':'list'})),
    path("users/create/", UserView.as_view({'post':'create'})),
    path("users/update/<int:pk>/", UserView.as_view({'put':'update', 'patch':'partial_update'})),
    path("users/delete/<int:pk>/", UserView.as_view({'delete':'destroy'})),
]