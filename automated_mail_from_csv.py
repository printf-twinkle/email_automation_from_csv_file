from pandas import *
import smtplib, ssl

df = read_csv('filename.csv')  # reads your csv file as a table (dataframe object)


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "**"  # Enter your address
receiver_emails = df['column_name'].tolist()
password = "**" # Enter your password
message = f"Subject:\n\n Body:... "
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_emails, message)
    print("mail sent")
