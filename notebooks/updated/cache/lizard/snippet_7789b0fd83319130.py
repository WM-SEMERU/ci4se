def docker2singularity(self, runscript='/bin/bash', force=False):
    recipe = ['Bootstrap: docker']
    recipe += ['From: %s' % self.fromHeader]
    recipe += self._create_section('files')
    recipe += self._create_section('labels')
    recipe += self._create_section('install', 'post')
    recipe += self._create_section('environ', 'environment')
    runscript = self._create_runscript(runscript, force)
    recipe += finish_section(runscript, 'runscript')
    if self.test is not None:
        recipe += finish_section(self.test, 'test')
    return '\n'.join(recipe).replace('\n\n', '\n')