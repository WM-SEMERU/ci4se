def do_execute(self):
    fname = self.input.payload
    data = serialization.read_all(fname)
    if len(data) == 1:
        if is_instance_of(data[0], 'weka.classifiers.Classifier'):
            cont = ModelContainer(model=Classifier(jobject=data[0]))
        elif is_instance_of(data[0], 'weka.clusterers.Clusterer'):
            cont = ModelContainer(model=Clusterer(jobject=data[0]))
        else:
            return 'Unhandled class: ' + classes.get_classname(data[0])
    elif len(data) == 2:
        if is_instance_of(data[0], 'weka.classifiers.Classifier'):
            cont = ModelContainer(model=Classifier(jobject=data[0]), header
                =Instances(data[1]))
        elif is_instance_of(data[0], 'weka.clusterers.Clusterer'):
            cont = ModelContainer(model=Clusterer(jobject=data[0]), header=
                Instances(data[1]))
        else:
            return 'Unhandled class: ' + classes.get_classname(data[0])
    else:
        return 'Expected 1 or 2 objects, but got ' + str(len(data)
            ) + ' instead reading: ' + fname
    self._output.append(Token(cont))
    return None