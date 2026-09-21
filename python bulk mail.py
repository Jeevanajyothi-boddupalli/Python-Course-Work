import smtplib
from email.message import EmailMessage

sender = "jeevanajyothiboddupalli@gmail.com"
password = "vafs tenh fkmm qnmi" 
receivers = ["jeevanajyothiboddupalli@gmail.com"]

file_path = "perfect_numbers.txt" 

with open(file_path, "rb") as f:
    file_data = f.read()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

for receiver in receivers:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "First Three Perfect Numbers"
    msg.set_content("""Hi,

I am sending the first three perfect numbers as a text file attachment.

Please find the attachment.

Thanks & Regards,
Jeevana Jyothi
""")
    msg.add_attachment(file_data, maintype="text", subtype="plain", filename="perfect_numbers.txt")
    server.send_message(msg)

server.quit()
print("Mails Sent Successfully!")