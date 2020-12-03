from django.urls import path
from . import views


urlpatterns = [
     path('',views.home_view,name='home'),
     path('home/',views.home_view,name='home'),
     path('index/',views.get_value,name='index'),
     path('login/',views.login_view,name='login'),
     path('studentlist/',views.student_list,name='list'),
     path('xlsheet/',views.export_users_xls,name='xlsheet'),
     path('emailPage/',views.emailPage,name='emailPage'),
     path('email_send/',views.email_send,name='email_send'),
     path('logout/',views.logout_view,name='logout')




]
