# alerts.py

import logging
import smtplib
from email.message import EmailMessage

def send_email_alert(subject, body, to_email, from_email='alerts@example.com'):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        # For demonstration, using localhost SMTP
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)

        logging.info(f"Alert sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")
        print(f"Alert error: {e}")

def alert_to_console_or_log(message):
    # Fallback for dev/testing
    logging.warning(f"ALERT: {message}")
    print(f"ALERT: {message}")
