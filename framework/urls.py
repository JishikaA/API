from django.urls import path

from framework import views

urlpatterns = [
    path('test',views.test,name='test'),
    path('snippet_list',views.snippet_list,name='snippet_list'),
    path('student_mark',views.student_mark,name='student_mark'),
    path('crud/<int:id>',views.crud,name='crud'),
    path('crud_employee/<int:id>',views.crud_employee,name='crud_employee')
]
