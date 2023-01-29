from django.urls import path

from Studentapp import views

urlpatterns =[
path('',views.log_fun,name='log'),                                     # it will display login.html page
path('reg',views.reg_fun,name='reg'),                          # it will redirect to register.html page
path('regdata',views.regdata_fun),                      # it will create superuser account
path('logdata',views.log_data),                          # it will read the data and verify user is superuser or not
path('home',views.home_fun,name='home'),                                                            # and redirect to home.html
path('add_students',views.addstudent_fun,name='add'),
path('read_data',views.read_data_fun),                       # it will insert record into student table
path('displays',views.display_fun,name='display'),              # it will display student table data in display.html page
path('update/<int:id>',views.update_fun,name='up'),            # it will update stdent data
path('delete/<int:id>',views.delete_fun,name='del'),              # it will delete record from table
path('logout',views.logout_fun,name='log_out'),

]