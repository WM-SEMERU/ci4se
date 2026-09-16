def reduceByWindow(self, reduceFunc, invReduceFunc, windowDuration,
    slideDuration):
    keyed = self.map(lambda x: (1, x))
    reduced = keyed.reduceByKeyAndWindow(reduceFunc, invReduceFunc,
        windowDuration, slideDuration, 1)
    return reduced.map(lambda kv: kv[1])