from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import smtplib
from email.message import EmailMessage
import os
import json
import logging
from datetime import datetime, timezone

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'sushil-portfolio-dev-secret-key-2026')

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MESSAGES_FILE = os.path.join(os.path.dirname(__file__), 'contact_messages.json')

def save_message_locally(name, email, message):
    """Save message locally so submissions are never lost even if SMTP fails or is not configured."""
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'name': name,
        'email': email,
        'message': message
    }
    try:
        messages = []
        if os.path.exists(MESSAGES_FILE):
            with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
                try:
                    messages = json.load(f)
                except json.JSONDecodeError:
                    messages = []
        messages.append(entry)
        with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved contact message locally from {name} ({email})")
    except Exception as e:
        logger.error(f"Failed to save message locally: {e}")

def send_email_notification(name, sender_email, message_body):
    """Send an email notification safely with EmailMessage."""
    mail_username = os.environ.get('MAIL_USERNAME', 'wantech010@gmail.com')
    mail_password = os.environ.get('EMAIL_PASS')
    mail_recipient = os.environ.get('MAIL_RECIPIENT', 'sushilyogi56@gmail.com')
    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))

    if not mail_password:
        logger.warning("EMAIL_PASS environment variable not set. Email notification skipped; saved locally.")
        return False

    try:
        msg = EmailMessage()
        msg['Subject'] = f"New Portfolio Message from {name}"
        msg['From'] = mail_username
        msg['To'] = mail_recipient
        msg['Reply-To'] = sender_email
        msg.set_content(f"""New message received from your portfolio website:

Name: {name}
Email: {sender_email}

Message:
{message_body}
""")

        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.starttls()
            server.login(mail_username, mail_password)
            server.send_message(msg)

        logger.info(f"Email successfully sent for contact message from {email}")
        return True
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        return False

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/submit_form', methods=['GET', 'POST'], endpoint='submit_form')
@app.route('/form', methods=['GET', 'POST'], endpoint='form')
def submit_form():
    if request.method == 'POST':
        # Support both form data and JSON data
        if request.is_json:
            data = request.get_json() or {}
        else:
            data = request.form.to_dict()

        name = (data.get('name') or '').strip()
        email = (data.get('email') or '').strip()
        message = (data.get('message') or '').strip()

        # Basic validation
        if not name or not email or not message:
            error_msg = "Please fill in all required fields (Name, Email, Message)."
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
                return jsonify({'status': 'error', 'message': error_msg}), 400
            flash(error_msg, 'danger')
            return redirect(url_for('home_page') + '#section-contact')

        if '@' not in email or '.' not in email.split('@')[-1]:
            error_msg = "Please provide a valid email address."
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
                return jsonify({'status': 'error', 'message': error_msg}), 400
            flash(error_msg, 'danger')
            return redirect(url_for('home_page') + '#section-contact')

        # Always save locally first so no user message is lost
        save_message_locally(name, email, message)

        # Attempt to deliver email if credentials configured
        email_sent = send_email_notification(name, email, message)

        success_msg = "Thank you! Your message has been sent successfully. I will get back to you soon."
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
            return jsonify({'status': 'success', 'message': success_msg})

        flash(success_msg, 'success')
        return redirect(url_for('home_page') + '#section-contact')

    # If accessed via GET, redirect gracefully to home contact section
    return redirect(url_for('home_page') + '#section-contact')

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("404.html"), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
