from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.category, name='category'),
    path('posts', views.post, name='post'),
    path('postdetail/<str:slug>', views.post_details, name='post_detail'),
    path('category/posts/<int:id>', views.cat_post, name='cat_post'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/setting/<int:id>', views.setting, name='setting'),
    path("user/<int:id>", views.user, name="user"),
    path('upload/post', views.upload_post, name='upload_post'),
    path("cat/delete/<str:slug>", views.cat_post_delete, name="cat_delete"),
    path("post/delete/<str:slug>", views.post_delete, name="post_delete"),
    path("user/delete/<str:slug>", views.user_post_delete, name="user_post_delete"),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("accounts/password_change/", auth_views.PasswordChangeView.as_view(template_name='password-change.html'), name="password_change"),
    path("accounts/password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='password-change-done.html'), name="password_change_done"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    path('test', views.test,name='test'),
]