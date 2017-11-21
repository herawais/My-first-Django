from django.conf.urls import url
from polls import views
urlpatterns = [
    url(r'^help/$', views.help, name='help'),
    url(r'^$', views.index, name='index'),
    url(r'^add-student/$', views.add_student),
    url(r'^add/$', views.add),
    #url(r'^help', views.help,   name='help'),
]
