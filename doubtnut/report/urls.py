from doubtnut.report import views
from django.conf.urls import url, include, re_path

urlpatterns = [
    re_path(r'^test-url/', views.TestView.as_view(), name="report"),
]
