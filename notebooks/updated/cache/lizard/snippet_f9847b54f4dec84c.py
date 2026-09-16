def encoded(self):
    self.update_preferences()
    fp = BytesIO()
    zipped = zipfile.ZipFile(fp, 'w', zipfile.ZIP_DEFLATED)
    path_root = len(self.path) + 1
    for base, dirs, files in os.walk(self.path):
        for fyle in files:
            filename = os.path.join(base, fyle)
            zipped.write(filename, filename[path_root:])
    zipped.close()
    return base64.b64encode(fp.getvalue()).decode('UTF-8')