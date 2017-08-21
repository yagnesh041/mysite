from django.conf.urls import url, include
from . import views


urlpatterns = [
url(r'^index$', views.index, name='index'),
url(r'^(?P<course_no>\d+)$',views.detail, name='detail'),
url(r'^grid$', views.directory_grid, name='directory_grid'),
url(r'^list$', views.directory_list, name='directory_list'),
url(r'^register$', views.register, name='sign_up'),
url(r'^mycourses$', views.mycourses, name='mycourses'),
url(r'^login$', views.user_login, name='user_login'),
url(r'^login$', views.user_logout, name='user_logout'),
url(r'^take_course/(?P<course_no>\d+)$',views.take_course,name='take_course'),
]
