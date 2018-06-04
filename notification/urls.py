from django.urls import path

from .views import notices, mark_all_seen, feed_for_user, single, notice_settings


urlpatterns = ["",
    path(r"^$", notices, name="notification_notices"),
    path(r"^settings/$", notice_settings, name="notification_notice_settings"),
    path(r"^(\d+)/$", single, name="notification_notice"),
    path(r"^feed/$", feed_for_user, name="notification_feed_for_user"),
    path(r"^mark_all_seen/$", mark_all_seen, name="notification_mark_all_seen"),
]
