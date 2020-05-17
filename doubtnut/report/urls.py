from doubtnut.report import views
from django.conf.urls import url, include, re_path

urlpatterns = [
    re_path(r'^summary/', views.SummaryAPI.as_view(), name="report"),
]
