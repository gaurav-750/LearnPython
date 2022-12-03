from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path

# *For attaching image
from email.mime.image import MIMEImage

# * For sending templates
from string import Template

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Gaurav J Somani"
message["to"] = "jonnyroy789@gmail.com"
message["subject"] = "Sending mail with Python"

body = template.substitute({
    "name": "John"
})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("GauravSomani_Pic.png").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("gauravsomani52750@gmail.com", "wwelxydkzgvryosr")
    smtp.send_message(message)
    print("Email sent successfully!")
