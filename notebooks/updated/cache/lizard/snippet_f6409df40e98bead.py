def fullData(master):
    builders = []
    for b in master.config.builders:
        steps = []
        for step in b.factory.steps:
            steps.append(getName(step))
        builders.append(steps)
    return {'builders': builders}