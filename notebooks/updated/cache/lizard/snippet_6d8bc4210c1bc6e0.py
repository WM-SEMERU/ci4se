def getSubdirectories(d):
    return [f for f in os.listdir(d) if os.path.isdir(os.path.join(d, f))]