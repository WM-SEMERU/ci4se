def reset(self):
    self.overall = {'Nref': 0.0, 'Nsys': 0.0, 'Nsubs': 0.0, 'Ntp': 0.0,
        'Nfp': 0.0, 'Nfn': 0.0}
    self.class_wise = {}
    for class_label in self.event_label_list:
        self.class_wise[class_label] = {'Nref': 0.0, 'Nsys': 0.0, 'Ntp': 
            0.0, 'Ntn': 0.0, 'Nfp': 0.0, 'Nfn': 0.0}
    return self