def check_env(self, envar, value):
    if value is None:
        bot.error('You must export %s to use Discourse' % envar)
        print('https://vsoch.github.io/helpme/helper-discourse')
        sys.exit(1)