import smtplib, ssl


def send_email(receiver_email,message):
    port = 465  # For SSL
    password = 'bath2020'
    sender_email = 'chain.app.ai@gmail.com'
    

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)