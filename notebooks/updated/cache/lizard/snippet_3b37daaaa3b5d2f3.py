def from_overlays(overlays):
    jc = JobConfig()
    jc.comment = overlays.get('comment')
    if 'jobConfigOverlays' in overlays:
        if len(overlays['jobConfigOverlays']) >= 1:
            jco = copy.deepcopy(overlays['jobConfigOverlays'][0])
            if 'jobConfig' in jco:
                _jc = jco['jobConfig']
                jc.job_name = _jc.pop('jobName', None)
                jc.job_group = _jc.pop('jobGroup', None)
                jc.preload = _jc.pop('preloadApplicationBundles', False)
                jc.data_directory = _jc.pop('dataDirectory', None)
                jc.tracing = _jc.pop('tracing', None)
                for sp in _jc.pop('submissionParameters', []):
                    jc.submission_parameters[sp['name']] = sp['value']
                if not _jc:
                    del jco['jobConfig']
            if 'deploymentConfig' in jco:
                _dc = jco['deploymentConfig']
                if 'manual' == _dc.get('fusionScheme'):
                    if 'fusionTargetPeCount' in _dc:
                        jc.target_pe_count = _dc.pop('fusionTargetPeCount')
                    if len(_dc) == 1:
                        del jco['deploymentConfig']
            if jco:
                jc.raw_overlay = jco
    return jc