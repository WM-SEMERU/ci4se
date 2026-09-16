def cmd(self):
    cmd = [self.compiler_binary] + self.flags + [('-U' + x) for x in self.undef
        ] + [('-D' + x) for x in self.define] + [('-I' + x) for x in self.
        include_dirs] + self.sources
    if self.run_linker:
        cmd += [('-L' + x) for x in self.library_dirs] + [(x if os.path.
            exists(x) else '-l' + x) for x in self.libraries] + self.linkline
    counted = []
    for envvar in re.findall('\\$\\{(\\w+)\\}', ' '.join(cmd)):
        if os.getenv(envvar) is None:
            if envvar not in counted:
                counted.append(envvar)
                msg = "Environment variable '{}' undefined.".format(envvar)
                self.logger.error(msg)
                raise CompilationError(msg)
    return cmd