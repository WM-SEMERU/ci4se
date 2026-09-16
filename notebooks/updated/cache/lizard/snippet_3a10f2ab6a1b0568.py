def start(self, autopush=True):
    if self.enabled:
        if autopush:
            self.push_message(self.message)
            self.spinner.message = ' - '.join(self.animation.messages)
        if not self.spinner.running:
            self.animation.thread = threading.Thread(target=_spinner, args=
                (self.spinner,))
            self.spinner.running = True
            self.animation.thread.start()
            sys.stdout = stream.Clean(sys.stdout, self.spinner.stream)