from django.urls import re_path

from .views import ReferView

urlpatterns = [
    re_path("refer/(?P<func>.*)/$", ReferView.as_view())
]
