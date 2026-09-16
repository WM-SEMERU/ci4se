def show(self, id):
    stats = self.stats()
    if stats:
        print('=' * 60)
        print('Profile of RDD<id=%d>' % id)
        print('=' * 60)
        stats.sort_stats('time', 'cumulative').print_stats()