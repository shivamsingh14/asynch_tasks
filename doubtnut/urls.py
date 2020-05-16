from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path, include

from doubtnut.report import views

urlpatterns = [
    re_path(r'api/v1/report/',   include(('doubtnut.report.urls', "report"), namespace='v1')),
]
