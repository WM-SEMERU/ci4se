def write_primers(primer_list, path, names=None, notes=None):
    if names is not None:
        if len(names) != len(primer_list):
            names_msg = 'Mismatch in number of notes and primers.'
            raise PrimerAnnotationError(names_msg)
        for i, name in enumerate(names):
            primer_list[i].name = name
    if notes is not None:
        if len(notes) != len(primer_list):
            notes_msg = 'Mismatch in number of notes and primers.'
            raise PrimerAnnotationError(notes_msg)
        for i, note in enumerate(notes):
            primer_list[i].note = note
    with open(path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'sequence', 'notes'])
        for primer in primer_list:
            string_rep = str(primer.overhang).lower() + str(primer.anneal)
            writer.writerow([primer.name, string_rep, primer.note])