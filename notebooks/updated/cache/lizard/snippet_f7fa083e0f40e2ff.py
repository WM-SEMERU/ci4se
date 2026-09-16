def prepareSwarm(self, predictedField=None, swarmParams=None):
    csvPath, workingDirPath = self.populateCsv()
    swarmDescriptionPath = os.path.join(workingDirPath,
        'swarm_description.json')
    self.writeSwarmDescription(csvPath, swarmDescriptionPath,
        predictedField=predictedField, swarmParams=swarmParams)