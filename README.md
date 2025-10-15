# 📧 Gmail Bulk Email Sender (Python)

A simple and secure Python script for sending personalized bulk emails using **Gmail SMTP**.  
Built to automate follow-ups, feedback requests, and event thank-you emails — like the **TECHNOZIA Challenge Your Brain** feedback system by **Hacker Bytez**.

---

## 🚀 Features

- ✅ Send emails to multiple recipients (from a `.txt` file)  
- ✅ Supports **plain text** and **HTML** email formats  
- ✅ Secure login using **App Passwords** (not your Gmail password)  
- ✅ Handles connection errors gracefully  
- ✅ Logs success & failure for each recipient  
- ✅ Easy configuration and setup  

---

## 📂 Project Structure

```

📁 gmail-bulk-sender
├── send_email.py          # Main Python script
├── gmail.txt              # List of recipient emails (one per line)
├── .env                   # Environment variables (optional)
└── README.md              # Documentation

````

---

## ⚙️ Prerequisites

Before running the script, make sure you have:

- 🐍 **Python 3.7+**
- 📦 Required libraries:
```bash
  pip install smtplib email
```

*(Already included in Python standard library, no extra install usually needed)*

---

## 🔐 Gmail Setup (App Password)

Since Google blocks less-secure login attempts, you must use a Gmail **App Password**:

1. Turn on **2-Step Verification** for your Gmail account.
   👉 [Google Account Security](https://myaccount.google.com/security)

2. Under **App passwords**, create a new password:

   * Select **Mail** as the app.
   * Select **Other (Custom name)** → e.g., `Python Bulk Mailer`.
   * Copy the 16-character password (ignore spaces).

3. Store it securely (see below).

---

## 🧰 Environment Configuration

Instead of hardcoding credentials, store them as environment variables.

### Linux / macOS

```bash
export SENDER_EMAIL="your_email@gmail.com"
export APP_PASSWORD="your_16_char_app_password"
```

### Windows (PowerShell)

```powershell
setx SENDER_EMAIL "your_email@gmail.com"
setx APP_PASSWORD "your_16_char_app_password"
```

Or, you can create a `.env` file and load it with `python-dotenv` (optional).

---

## 📝 How to Use

1. Add your recipient emails to `gmail.txt` (one per line):

   ```
   example1@gmail.com
   example2@gmail.com
   example3@gmail.com
   ```

2. Edit the email content in `send_email.py`:

   * Change the **subject**, **plain text body**, or **HTML body**.

3. Run the script:

   ```bash
   python3 send_email.py
   ```

4. The console will show:

   ```
   ✅ Email sent to example1@gmail.com
   ✅ Email sent to example2@gmail.com
   All send attempts finished.
   ```

---

## 💡 Example Email Content

**Subject:** Thank You for Your Feedback!

**Body:**

```
Hi there,

Thank you for participating in TECHNOZIA – Challenge Your Brain! 🎉
We hope you enjoyed the quiz and had a great time challenging your brain.

Your feedback helps us improve future events.

Best regards,
Uday Raut
Founder, Hacker Bytez
```

---

## ⚠️ Important Notes

* Never hardcode your Gmail credentials in the script.
* Always use App Passwords (not your main Gmail password).
* Gmail limits the number of emails sent per day (~500 for personal accounts).
* Avoid sending too quickly — add a short delay (e.g., 0.5–1s between sends).
* Test with a few emails first before large batches.

---

## 🧠 About Hacker Bytez

**Hacker Bytez** is a tech-learning platform created by **Uday Raut**, focused on coding challenges, quizzes, and hands-on technical content.
Visit 🌐 [https://www.hackerbytez.com](https://www.hackerbytez.com)

---

## 📜 License

This project is licensed under the **MIT License** — feel free to modify and use it responsibly.

---

## 👨‍💻 Author

**Uday Raut**
Founder — [Hacker Bytez](https://www.hackerbytez.com)
📧 [hackerbytez128@gmail.com](mailto:hackerbytez128@gmail.com)
 
