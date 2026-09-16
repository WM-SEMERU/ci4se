def init(self):
    import subprocess
    import fcntl
    width = str(self.image_dimensions[0])
    height = str(self.image_dimensions[1])
    comlist = self.executable.split() + [width, height, self.tmpfile]
    try:
        self.p = subprocess.Popen(comlist, stdout=subprocess.PIPE, stdin=
            subprocess.PIPE)
    except Exception as e:
        print(self.pre, "Could not open external process.  Failed with '" +
            str(e) + "'")
        return
    self.reset()