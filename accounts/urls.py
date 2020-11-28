from django.urls import path

from . import views
 
urlpatterns=[
    path("register",views.register ,name="register"),
    path("login",views.login, name="login"),
    path("trade",views.trade, name="trade"),
    path("scripttrade",views.scripttrade, name="scripttrade"),
    #path("globalindices",views.globalindices, name="globalindices")
    

    ]