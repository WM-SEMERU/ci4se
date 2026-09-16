async def send_with_attachments(subject, message, filepaths, config):
    email_ = MIMEMultipart()
    email_.attach(MIMEText(message))
    email_['Subject'] = subject
    email_['From'] = get_attribute_from_config(config, EMAIL_SECTION_KEY,
        USER_KEY)
    email_['To'] = get_attribute_from_config(config, EMAIL_SECTION_KEY,
        RECEIVER_KEY)
    _attach_files(filepaths, email_)
    await _send_email(email_, config)