from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', (WomenHome.as_view()), name='home'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(extra_context={'title': "Список по категориям"}), name='category'),
    path('logout/', logout_user, name='logout'),
    path('favorites/', favourite_list, name='favourite_list'),
    path('fav/<int:id>', favourite_add, name='favourite_add'),
]

