
from os import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.ShowLoginPage,name="showlogin"),
    path('signup/',views.IndexPage,name='signup'),
    path("insertuser/",views.InsertUser,name='insertuser'),
    path('home/',views.LoginUser,name="homepage"),
    path('insert/',views.InsertCustomer,name='insertpage'),
    path('delete/<int:pk>',views.Delete,name="delete"),
    path('edit/<int:pk>',views.Editpage,name="editpage"),
    path('editUser/<int:pk>',views.EditUser,name="editUser"),
    path('search/',views.SearchCustomer,name="searchpage"),
    path('detail/<int:pk>',views.DetailPage,name="detailpage"),
    path('superuser/',views.SuperuserOp,name="SuperuserOp"),
    path('deleteSuper/<int:sn>',views.DeleteSuper,name="DeleteSuper"),
    path('calculator/',views.ShowCal,name="calpage"),
    path('calculated/',views.Calculator,name="calculated"),
    path('speak1/',views.command1,name="speak1"),
    
]