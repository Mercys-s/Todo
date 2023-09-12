from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Auth
    path('signup/' , views.signupuser , name = 'signupuser' ),
    path('logout/' , views.logoutuser , name = 'logoutuser' ),  # type: ignore
    path('login/' , views.loginuser , name = 'loginuser' ),

    #todo
    path('' , views.home , name = 'home' ),
    path('create/' , views.createtodo , name = 'createtodo' ),
    path('current/' , views.currenttodos , name = 'currenttodos' ),
    path('completed/' , views.completedtodos , name = 'completedtodos' ),
    path('todo/<int:todo_pk>' , views.viewtodo , name = 'viewtodo' ),
    path('todo/<int:todo_pk>/complete' , views.completetodo , name = 'completetodo' ),  # type: ignore
    path('todo/<int:todo_pk>/delete' , views.deletetodo , name = 'deletetodo' ),  # type: ignore

]
