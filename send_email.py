from email.mime.text import MIMEText
import smtplib

def send_email(email,df):
    from_email="suraj013786@gmail.com"
    from_password="suraj013"
    to_email=email

    subject ="GeoCoder Co-Ordinates"

    html = """\
    <html>
    <head></head>
    <body>
    {0}
    </body>
    </html>
    """.format(df.to_html())

    msg = MIMEText(html, 'html')

    #message="Hey there, your Height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Thanks!" % (height, average_height, count)
    #list=df.values.tolist()
    #list=df.to_string()
    #message="Hey there, Below are the Co-Ordintes of your uploaded File <br><br> <strong>%s</strong>. <br><br> Thanks!" % (list)
    #msg=MIMEText(message, 'html')
    #msg = df.to_html()
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
