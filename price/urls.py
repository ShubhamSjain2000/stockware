from django.urls import path

from . import views
 
urlpatterns=[path("",views.index,name="index"),
path("scripts",views.scripts, name="scripts"),
path("globalindices",views.globalindices,name="globalindices"),
path("research",views.research,name="research"),
path("contact",views.contact,name="contact"),
path("profile",views.profile,name="profile"),
path("holdings",views.holdings,name="holdings"),
path("app",views.app,name="app")


]