import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_info():
    teacher_name = input("Enter the name of the teacher: ")
    email = input("Enter the parent email address: ")
    date = input("Enter the start date of the class: ")
    week_day = input("Enter the day of the week the class is on: ")
    class_time = input("Enter the time the class starts: ")
    timezone = input("Enter the timezone of the class: ")
    if not timezone:
        timezone = "Eastern Time"
    class_type = input("Enter the type of class: ")
    payment_type = {
        'group': "https://kakaaki.com/payment",
        'private': "https://kakaaki.com/payment-one-to-one",
        "group_old":"https://kakaaki.com/old-payment",
        "private_old":"https://kakaaki.com/old-payment-one-to-one"
    }
    
    return teacher_name,email, date, week_day, class_time, timezone, payment_type[class_type.lower()]


def get_teacher(teacher_name):
    rabi_sir = {
        "name":"Rabi Sir (Full name - Rabi Khakurel)",
        "zoom_link": "https://us04web.zoom.us/j/3862315475?pwd=cjV5d0k1NUtlWS9KTmdiMXFTS1pWQT09"
    }
    sarita_mam = {
        "name":"Sarita Madam (Full name - Sarita Adhikari)",
        "zoom_link": "https://us04web.zoom.us/j/6562215329?pwd=d2NpV0tnRkdsMy9PZ0xTRFVMMDRBUT09"
    }
    shova_mam = {
        "name":"Shova Madam (Full name - Shova Baskota)",
        "zoom_link": "https://us04web.zoom.us/j/6919245192?pwd=UjB0M1c2MG9EZldJNWhGSlFIVW1oUT09"
    }
    anju_mam = {
        "name":"Anju Madam (Full name - Anju Adhikari)",
        "zoom_link": "https://zoom.us/j/7582103255?pwd=Vi9ZaW9YQVZFTGkzQTF3RlV3SmFMdz09"
    }
    parbati_mam = {
        "name":"Parbati Madam (Full name - Parbati Bista)",
        "zoom_link": "https://us04web.zoom.us/j/8464341785?pwd=hNxQENSZVjkbo3BXJXChtIvDtvb-EQ"
    }
    reeta_mam = {
        "name":"Reeta Madam (Full name - Reeta Aryal)",
        "zoom_link": " https://us04web.zoom.us/j/6475642002?pwd=WjRFZnhNMmVjRWRPVlpkVXdRaUhUQT09"
    }
    santoshi_mam = {
        "name":"Santoshi Madam (Full name - Santoshi Khatiwada)",
        "zoom_link": "https://us04web.zoom.us/j/6471879079?pwd=JnEyxBSzalPqJlxD7aasZhhtCaWzEt.1"
    }
    shiwani_mam = {
        "name":"Shiwani Madam (Full name - Shiwani Ghimire)",
        "zoom_link": "https://us06web.zoom.us/j/7601411307?pwd=TzAjlHiCa5saOOsBK2uaghxktR26DZ.1"
    }
    teacher_details = {
        'rabi': rabi_sir,
        'sarita': sarita_mam,
        'shova': shova_mam,
        'anju': anju_mam,
        'parbati': parbati_mam,
        'reeta': reeta_mam,
        'santoshi': santoshi_mam,
        'shiwani': shiwani_mam
    }
    
    return teacher_details[teacher_name.lower()]



def get_template_data():
    teacher_name,email, date, week_day, class_time, timezone, payment = get_info()
    teacher = get_teacher(teacher_name)
    template_data = {
        'teacher_name': teacher['name'],
        'zoom_link': teacher['zoom_link'],
        'start_date': date,
        'week_day': week_day,
        'class_time': class_time,
        'timezone': timezone,
        'payment_link': payment
    }
    return email, template_data




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
















































    
    