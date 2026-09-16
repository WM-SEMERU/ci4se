def getEAnnotation(self, source):
    for annotation in self.eAnnotations:
        if annotation.source == source:
            return annotation
    return None