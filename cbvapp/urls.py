from django.conf.urls import url
from cbvapp import views

app_name='cbvapp'

urlpatterns = [
    url('collageList/',views.collageList.as_view(),name='list')
]
