from django.urls import path, re_path

from .views import notices, mark_all_seen, feed_for_user, single, notice_settings, unseen_count


urlpatterns = [
    path("", notices, name="notification_notices"),
    path("settings/", notice_settings, name="notification_notice_settings"), # Template is missing
    re_path(r"^(\d+)/$", single, name="notification_notice"),
    path("feed/", feed_for_user, name="notification_feed_for_user"),
    path("mark_all_seen/", mark_all_seen, name="notification_mark_all_seen"),
    path("unseen_count/", unseen_count, name="notification_unseen_count"),
]
