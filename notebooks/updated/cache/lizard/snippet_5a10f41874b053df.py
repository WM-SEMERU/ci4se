def get_patient_expression(job, patient_dict):
    expression_archive = job.fileStore.readGlobalFile(patient_dict[
        'expression_files'])
    expression_archive = untargz(expression_archive, os.getcwd())
    output_dict = {}
    for filename in ('rsem.genes.results', 'rsem.isoforms.results'):
        output_dict[filename] = job.fileStore.writeGlobalFile(os.path.join(
            expression_archive, filename))
    return output_dict