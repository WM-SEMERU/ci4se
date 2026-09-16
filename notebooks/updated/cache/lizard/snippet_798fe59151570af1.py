def run_gradle(path=kernel_path, cmd='build', skip_tests=False):


    class Gradle(BaseCommand):
        description = 'Run gradle script'

        def skip_test_option(self, skip):
            if skip:
                return '-Dskip.tests=True'
            else:
                return '-Dskip.tests=False'

        def run(self):
            run([('' if sys.platform == 'win32' else './') + 'gradlew',
                '--no-daemon', cmd, self.skip_test_option(skip_tests)], cwd
                =path)
    return Gradle