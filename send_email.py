import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor, as_completed
from decouple import config

def get_html_file_path():
    email_type = input("Enter the email type (class/payment): ")
    if email_type == "class":
        file_path = '/Users/sauravaryal/Developer/projects/email_formats/class_email.html'
        subject = "Kakaaki Class Inforamtion"
        from class_email import get_template_data
        template_data = get_template_data()
    elif email_type == "payment":
        file_path = '/Users/sauravaryal/Developer/projects/email_formats/payment_email.html'
        subject = "Kakaaki Payment Due"
        from payment_email import get_template_data
        template_data = get_template_data()
    
    return file_path,subject,template_data

# Function to read the HTML template from a file
def read_html_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_template = file.read()
    return html_template


html_file_path,subject,datas = get_html_file_path()
html_template = read_html_template(html_file_path)

receiver_email,template_data = datas




# Function to send email using Outlook
def send_email(email, subject, html_template, template_data):
    # Replace placeholders in the HTML template with actual data
    body_html = html_template.format(**template_data)
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'info@kakaaki.com'
    msg['To'] = email

    # Attach the HTML content to the email
    msg.attach(MIMEText(body_html, 'html'))

    # Send the email using Outlook's SMTP server
    try:
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587

        sender_email = 'info@kakaaki.com'
        password = config('EMAIL_PASSWORD')

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")




with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(send_email, email, subject, html_template, template_data) for email in receiver_email]

        
        








































    
    