def get_exp_of_biosample(biosample_rec):
    chip_exp_id = biosample_rec.chipseq_experiment_id
    ssc_id = biosample_rec.sorting_biosample_single_cell_sorting_id
    if chip_exp_id:
        return {'type': 'chipseq_experiment', 'record': models.
            ChipseqExperiment(chip_exp_id)}
    elif ssc_id:
        return {'type': 'single_cell_sorting', 'record': models.
            SingleCellSorting(ssc_id)}
    raise Exception('Biosample {} is not on an experiment.'.format(
        biosample_rec['id']))