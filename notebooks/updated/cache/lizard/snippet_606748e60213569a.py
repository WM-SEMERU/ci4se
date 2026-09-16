def stop(self):
    if self.uiautomator_process and self.uiautomator_process.poll() is None:
        res = None
        try:
            res = urllib2.urlopen(self.stop_uri)
            self.uiautomator_process.wait()
        except:
            self.uiautomator_process.kill()
        finally:
            if res is not None:
                res.close()
            self.uiautomator_process = None
    try:
        out = self.adb.cmd('shell', 'ps', '-C', 'uiautomator').communicate()[0
            ].decode('utf-8').strip().splitlines()
        if out:
            index = out[0].split().index('PID')
            for line in out[1:]:
                if len(line.split()) > index:
                    self.adb.cmd('shell', 'kill', '-9', line.split()[index]
                        ).wait()
    except:
        pass