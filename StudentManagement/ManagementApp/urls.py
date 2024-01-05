from django.urls import path
from ManagementApp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    #registration
    path('studentregister',views.student_register,name='student_register'),
    path('teacherregister',views.teacher_register,name='teacher_register'),
    
    #dashboard
    path('admindashboard',views.admin_dashboard,name='admin_dashboard'),
    path('studentdashboard',views.student_dashboard,name='student_dashboard'),
    path('teacherdashboard',views.teacher_dashboard,name='teacher_dashboard'),
    
    #approval section
    path('studentapproval',views.student_approval,name='student_approval'),
    path('approve/<int:id>',views.approval,name='approval'),
    
    #profile of teacher
    path('teacherprofile',views.teacher_profileview,name='teacher_profileview'),
    path('teacherprofileupdate',views.teacher_profileupdate1,name='teacher_profileupdate1'),
    path('teacherprofileupdate1/<int:uid>',views.teacher_profileupdate2,name='teacher_profileupdate'),
    
    #student_profile
    path('studentprofile',views.student_profileview,name='student_profileview'),
    path('studentprofileupdate',views.student_profileupdate1,name='student_profileupdate1'),
    path('studentprofileupdate1/<int:uid>',views.student_profileupdate2,name='student_profileupdate'),
    
    #teacher_list_view_and_edit
    path('teacherlistview',views.teacher_listview,name='teacher_listview'),
    path('teacherdelete/<int:uid>',views.teacher_delete,name='teacher_delete'),
    path('teacheredit/<int:uid>',views.teacher_edit,name='teacher_edit'),
    
    #student_list_view_and_edit
    path('studentlistview',views.student_listview,name='student_listview'),
    path('studentdelete/<int:uid>',views.student_delete,name='student_delete'),
    path('studentedit/<int:uid>',views.student_edit,name='student_edit'),
    
    
]