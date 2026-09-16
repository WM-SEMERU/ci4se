def _setup_message(self):
    if self.content == 'html':
        self._message = MIMEMultipart('alternative')
        part = MIMEText(self.body, 'html', 'UTF-8')
    else:
        self._message = MIMEMultipart()
        part = MIMEText(self.body, 'plain', 'UTF-8')
    self._message.preamble = 'Multipart massage.\n'
    self._message.attach(part)
    self._message['From'] = self.sender
    self._message['To'] = COMMASPACE.join(self.to)
    if self.cc:
        self._message['Cc'] = COMMASPACE.join(self.cc)
    self._message['Date'] = formatdate(localtime=True)
    self._message['Subject'] = self.subject
    for part in self._parts:
        self._message.attach(part)