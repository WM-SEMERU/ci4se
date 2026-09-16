def addChildJobFn(self, fn, *args, **kwargs):
    if PromisedRequirement.convertPromises(kwargs):
        return self.addChild(PromisedRequirementJobFunctionWrappingJob.
            create(fn, *args, **kwargs))
    else:
        return self.addChild(JobFunctionWrappingJob(fn, *args, **kwargs))