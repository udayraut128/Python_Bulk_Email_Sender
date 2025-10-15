import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------- CONFIGURATION ----------
sender_email = "hackerbytez128@gmail.com"
app_password = "giqx yles qhzj uoln"  # Gmail App password
subject = "Thank You for Your Feedback!"
body = """
Hi there,

Thank you for participating in TECHNOZIA – Challenge Your Brain! 🎉
We hope you enjoyed the quiz and had a great time challenging your brain.

Your feedback is extremely valuable to us. By sharing your thoughts, suggestions, or any issues you faced, you help us make our quizzes and events even better in the future.

💡 About Our Website:
Hacker Bytez (https://www.hackerbytez.com) is a platform where we share exciting quizzes, coding challenges, and technical content for students and enthusiasts. Our goal is to promote learning, creativity, and healthy competition among tech enthusiasts.

We truly appreciate your time and support in making TECHNOZIA a success!

Thank you once again for participating. We look forward to your feedback: https://www.hackerbytez.com/feedback

Best regards,
Uday Raut
Founder, Hacker Bytez,
All AGC Computer Engineers Society (ACES) Members
"""


# ---------- READ EMAILS ----------
with open("gmail.txt", "r") as f:
    recipients = [line.strip() for line in f if line.strip()]

# ---------- SEND EMAIL ----------
try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"✅ Email sent to {recipient}")

    server.quit()
    print("All emails sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")

