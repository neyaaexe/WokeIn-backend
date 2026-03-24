from app.services.auth_service import register_user, login_user, verify_token

def test_register_login_verify():
    user_id = register_user("test@example.com", "password", "user")
    token, uid = login_user("test@example.com", "password", "user")
    assert uid == user_id
    user = verify_token(token)
    assert user["email"] == "test@example.com"