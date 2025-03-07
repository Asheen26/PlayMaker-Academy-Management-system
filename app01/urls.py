from django.urls import path,include
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('Player Registration/',views.player_registration,name='player_registration'),
    path('staff Registration/',views.staff_registration,name='staff_registration'),
    path('login/',views.login,name='login'),
    path('landing/',views.landing,name='landing'),
    path('player_profile/',views.player_profile,name='player_profile'),
    path('logout/',views.logout,name='logout'),
    path('staff_landing/',views.staff_landing,name='staff_landing'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('coach_dashboard/',views.coach_dashboard,name='coach_dashboard'),
    path('medical_dashboard/',views.medical_dashboard,name='medical_dashboard'),
    path('analyst_dashboard/',views.analyst_dashboard,name='analyst_dashboard'),
    path('take_player_attendance/',views.take_player_attendance,name='take_player_attendance'),
    path('view_player_attendance/', views.view_player_attendance, name='view_player_attendance'),
    path('give_player_stats/', views.give_player_stats, name='give_player_stats'),
    path('view_player_stats/', views.view_player_stats, name='view_player_stats'),
    path('send-message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('upload-workload/', views.upload_workload, name='upload_workload'),
    path('view-workload/', views.view_workload, name='view_workload'),
    path('training-schedule/',views.training_schedule,name='training_schedule'),
    path('view-schedule/', views.view_schedule, name='view_schedule'),
    path('injury-management/', views.injury_management, name='injury_management'),
    path('injury/remove/<int:id>/', views.remove_injury, name='remove_injury'),
    path('active-injury-list/', views.active_injury_list, name='active_injury_list'),
    path('injury-history/', views.injury_history, name='injury_history'),
    path('player_list/', views.player_list, name='player_list'),
    path('list_player_profile/<int:id>/',views.list_player_profile,name='list_player_profile'),
    path('staff_profile/',views.staff_profile,name='staff_profile'),
    path('staff_list/',views.staff_list,name='staff_list'),
    path('list_staff_profile/<int:id>/',views.list_staff_profile,name='list_staff_profile'),

]