from notification.models import NoticeType


class TestNoticeType:
    def test_initiate_notice_type(self):
        n = NoticeType(label="test_label")
        assert str(n) == "test_label"
