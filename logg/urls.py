from django.conf.urls import url
from . import views

app_name = "loggy"

urlpatterns = [
    url(r'^logs$', views.show_logs, name="render_logs")
]
