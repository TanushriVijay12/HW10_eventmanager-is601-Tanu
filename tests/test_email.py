import pytest
from unittest.mock import patch
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager
from tests.dummy_smtp import DummySMTP
    
@pytest.mark.asyncio
async def test_send_markdown_email(email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }
    # Patch the SMTP class only for this test so DummySMTP is used.
    with patch("smtplib.SMTP", new=DummySMTP):
        await email_service.send_user_email(user_data, 'email_verification')
    # If no exception is raised, the test passes.