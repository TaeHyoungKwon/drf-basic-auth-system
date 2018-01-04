from django.conf.urls import url,include
from django.contrib import admin
from account.api.views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserDetailAPIView,
    UserDeleteAPIView,
    OnlyAdminUserListAPIView,
    OnlyAdminUserUpdateAPIView
    )


urlpatterns = [

    url(r'^register/$', UserCreateAPIView.as_view(), name='api-register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='api-login'),

    url(r'^user_list/$', UserListAPIView.as_view(), name='api-user-list'),
    url(r'^user_list/(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name='api-user-detail'),
    
    url(r'^user_list/(?P<pk>\d+)/edit/$', UserUpdateAPIView.as_view(), name='api-user-edit'),
    url(r'^user_list/(?P<pk>\d+)/delete/$', UserDeleteAPIView.as_view(), name='api-user-delete'),

    url(r'^customadmin/user_list/$', OnlyAdminUserListAPIView.as_view(), name='admin-api-user-list'),
    url(r'^customadmin/user_list/(?P<pk>\d+)/edit/$', OnlyAdminUserUpdateAPIView.as_view(), name='admin-api-user-list'),

]
