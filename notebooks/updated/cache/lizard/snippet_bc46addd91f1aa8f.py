def runStretchExperiment(numObjects=25):
    exp = L4L2Experiment('profiling_experiment', enableLateralSP=True,
        enableFeedForwardSP=True)
    objects = createObjectMachine(machineType='simple', numInputBits=20,
        sensorInputSize=1024, externalInputSize=1024)
    objects.createRandomObjects(numObjects=numObjects, numPoints=10)
    exp.learnObjects(objects.provideObjectsToLearn())
    exp.printProfile()
    inferConfig = {'numSteps': len(objects[0]), 'pairs': {(0): objects[0]}}
    exp.infer(objects.provideObjectToInfer(inferConfig), objectName=0)
    exp.printProfile()
    exp.plotInferenceStats(fields=['L2 Representation',
        'Overlap L2 with object', 'L4 Representation'])