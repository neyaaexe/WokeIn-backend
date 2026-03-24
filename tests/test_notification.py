from app.services.notification_service import add_notification, get_notifications

def test_notifications():
    add_notification("user1", "Test message", "info")
    notes = get_notifications("user1")
    assert any(n["message"] == "Test message" for n in notes)