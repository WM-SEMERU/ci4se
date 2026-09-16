def select_generic_executable(workflow, exe_tag):
    exe_path = workflow.cp.get('executables', exe_tag)
    exe_name = os.path.basename(exe_path)
    exe_to_class_map = {'ligolw_add': LigolwAddExecutable,
        'ligolw_cbc_sstinca': LigolwSSthincaExecutable,
        'pycbc_sqlite_simplify': PycbcSqliteSimplifyExecutable,
        'ligolw_cbc_cluster_coincs': SQLInOutExecutable,
        'ligolw_cbc_repop_coinc': SQLInOutExecutable, 'repop_coinc_expfit':
        SQLInOutExecutable, 'ligolw_cbc_dbinjfind': SQLInOutExecutable,
        'lalapps_inspinj': LalappsInspinjExecutable,
        'pycbc_dark_vs_bright_injections':
        PycbcDarkVsBrightInjectionsExecutable, 'pycbc_timeslides':
        PycbcTimeslidesExecutable, 'pycbc_compute_durations':
        ComputeDurationsExecutable, 'pycbc_calculate_far':
        PycbcCalculateFarExecutable, 'pycbc_run_sqlite': SQLInOutExecutable,
        'ligolw_sqlite': ExtractToXMLExecutable, 'pycbc_inspinjfind':
        InspinjfindExecutable, 'pycbc_pickle_horizon_distances':
        PycbcPickleHorizonDistsExecutable, 'pycbc_combine_likelihood':
        PycbcCombineLikelihoodExecutable, 'pycbc_gen_ranking_data':
        PycbcGenerateRankingDataExecutable, 'pycbc_calculate_likelihood':
        PycbcCalculateLikelihoodExecutable,
        'gstlal_inspiral_marginalize_likelihood':
        GstlalMarginalizeLikelihoodExecutable,
        'pycbc_compute_far_from_snr_chisq_histograms':
        GstlalFarfromsnrchisqhistExecutable,
        'gstlal_inspiral_plot_sensitivity': GstlalPlotSensitivity,
        'gstlal_inspiral_plot_background': GstlalPlotBackground,
        'gstlal_inspiral_plotsummary': GstlalPlotSummary,
        'gstlal_inspiral_summary_page': GstlalSummaryPage,
        'pycbc_condition_strain': PycbcConditionStrainExecutable}
    try:
        return exe_to_class_map[exe_name]
    except KeyError:
        raise NotImplementedError(
            'No job class exists for executable %s, exiting' % exe_name)