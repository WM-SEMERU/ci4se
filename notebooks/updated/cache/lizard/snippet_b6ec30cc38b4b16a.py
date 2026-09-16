def as_backfill_cron_app(cls):

    def main(self, function=None):
        return super(cls, self).main(function=function, once=False)
    cls.main = main
    cls._is_backfill_app = True
    return cls