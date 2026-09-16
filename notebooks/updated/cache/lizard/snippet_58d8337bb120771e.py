def save(self):
    file_name = fd.asksaveasfilename()
    if file_name is '' or file_name is None:
        return
    with open(file_name, 'w') as f:
        f.write(self.text.get('1.0', tk.END))