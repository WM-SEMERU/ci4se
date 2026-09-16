def removeReadGroupSet(self, readGroupSet):
    for readGroupSetRecord in models.Readgroupset.select().where(models.
        Readgroupset.id == readGroupSet.getId()):
        readGroupSetRecord.delete_instance(recursive=True)