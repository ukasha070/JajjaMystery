from django.core.mail import EmailMessage
from django.template.loader import render_to_string

import os
from dotenv import load_dotenv

load_dotenv()

TO_EMAIL_HOST = os.getenv("TO_EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")


def send_email_to_jajja(html_template, context):
    html_content = render_to_string(html_template, context)
    subject = "Message from website."

    from_email = EMAIL_HOST_USER

    email = EmailMessage(
        subject,
        html_content,
        from_email,  
        [TO_EMAIL_HOST],
    )

    email.content_subtype = 'html'
    email.send()



