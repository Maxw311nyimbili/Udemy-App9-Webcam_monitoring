import smtplib
import imghdr # gives meta-data about the image
from email.message import EmailMessage

PASSWORD = "zlur zkbo beys ooek"
SENDER = "zisacompanyltd@gmail.com"
RECIEVER = "zisacompanyltd@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    # body of the email
    email_message.set_content("Hey, we just got a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())


