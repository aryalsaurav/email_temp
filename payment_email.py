def get_info():
    emails = input("Enter the parent email address: ")
    class_type = input("Enter the type of class: ")
    payment_type = {
        'group': "https://kakaaki.com/payment",
        'private': "https://kakaaki.com/payment-one-to-one",
        "group_old":"https://kakaaki.com/old-payment",
        "private_old":"https://kakaaki.com/old-payment-one-to-one"
    }
    if emails:
        emails = emails.split(',')
    else:
        raise ValueError("Please enter the email address of the parent")
    return emails, payment_type[class_type.lower()]




def get_template_data():
    email, payment = get_info()
    template_data = {
        'payment_link': payment
    }
    return email, template_data