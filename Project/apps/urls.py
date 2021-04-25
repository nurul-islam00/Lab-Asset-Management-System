from  django.urls import path
from . import  views

urlpatterns = [
    path('', views.firstpage),
    path('admin_login',views.admin_login),
    path('student_registration',views.student_registration),
    path('confirm_registration',views.confirm_registration),
    path('instrument_registration',views.instrument_registration),
    path('confirm_ins_registration',views.confirm_ins_registration),
    path('assign_instrument', views.assign_instrument),
    path('confirm_ins_assign', views.confirm_ins_assign),
    path('collect_instrument', views.collect_instrument),
    path('confirm_ins_collect', views.confirm_ins_collect),
    path('student_list', views.student_list),
    path('instrument_list', views.instrument_list),
    path('student_search', views.student_search),
    path('instrument_search_admin', views.instrument_search_admin),
    path('home', views.home),
    path('student_login', views.student_login),
    path('student_login2', views.student_login2),
    path('instrument_list_s', views.instrument_list_s),
    path('home2', views.home2),
    path('profile', views.profile),
    path('student_list/delete/<id>/', views.delete),
    path('student_profile', views.student_profile),
    path('student_profile_search', views.student_profile_search),

]