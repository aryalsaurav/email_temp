import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText






# Function to read the HTML template from a file
def read_html_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_template = file.read()
    return html_template

# Function to send email using Outlook
def send_email(receiver_email, subject, html_template, template_data):
    # Replace placeholders in the HTML template with actual data
    body_html = html_template.format(**template_data)
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'info@kakaaki.com'
    msg['To'] = receiver_email

    # Attach the HTML content to the email
    msg.attach(MIMEText(body_html, 'html'))

    # Send the email using Outlook's SMTP server
    try:
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587

        sender_email = 'info@kakaaki.com'
        password = 'Test@123'

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Example usage
html_file_path = '/Users/sauravaryal/Developer/projects/email_formats/class_email.html'  # Path to your HTML template file
html_template = read_html_template(html_file_path)
subject = "Kakaaki Class Inforamtion"  # Email subject

receiver_email, template_data = get_template_data()

# Data to replace in the template

send_email(receiver_email, subject, html_template, template_data)
















































    
    