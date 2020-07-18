from django.conf.urls import url 
from basic_app import views 

app_name = 'basic_app'

urlpatterns = [
    url( r'^$', views.School_ListView.as_view(), name="list"),
    url(r'^(?P<pk>[-\w]+)/', views.School_DetailView.as_view(), name="detail")
]