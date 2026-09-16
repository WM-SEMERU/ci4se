def addFollowOnJobFn(self, fn, *args, **kwargs):
    if PromisedRequirement.convertPromises(kwargs):
        return self.addFollowOn(PromisedRequirementJobFunctionWrappingJob.
            create(fn, *args, **kwargs))
    else:
        return self.addFollowOn(JobFunctionWrappingJob(fn, *args, **kwargs))