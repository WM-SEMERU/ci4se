def execute_command(self):
    print(Back.GREEN + Fore.BLACK + 'Scrapple Web Interface')
    print(Back.RESET + Fore.RESET)
    p1 = Process(target=self.run_flask)
    p2 = Process(target=lambda : webbrowser.open('http://127.0.0.1:5000'))
    p1.start()
    p2.start()