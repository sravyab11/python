import smtplib
from email.message import EmailMessage
from datetime import datetime

# -------- STEP 1: Update file --------
file_name = "log.txt"

with open(file_name, "a") as file:
    file.write(f"Updated at: {datetime.now()}\n")

print("File updated successfully.")

# -------- STEP 2: Send email --------
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Not your real password

msg = EmailMessage()
msg['Subject'] = "Python Automation Update"
msg['From'] = EMAIL_ADDRESS
msg['To'] = "receiver_email@gmail.com"

msg.set_content("File has been updated successfully!")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("Email sent successfully.")

except Exception as e:
    print("Error sending email:", e)