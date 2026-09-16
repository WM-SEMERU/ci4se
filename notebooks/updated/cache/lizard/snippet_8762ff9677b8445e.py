def verify_submission(self, base_path, submission, update):
    results = VerificationResults()
    valid_files = set()
    file_mapping = submission.file_mapping()
    file_verifiers = set(fv for testable in self.testables for fv in
        testable.file_verifiers)
    for fv in file_verifiers:
        if fv.filename in file_mapping:
            errors, warnings = fv.verify(base_path, file_mapping[fv.filename])
            if errors:
                results.set_errors_for_filename(errors, fv.filename)
            else:
                valid_files.add(fv.filename)
            if warnings:
                results.set_warnings_for_filename(warnings, fv.filename)
            del file_mapping[fv.filename]
        elif not fv.optional:
            results.set_errors_for_filename(['missing'], fv.filename)
    if file_mapping:
        results.set_extra_filenames(frozenset(file_mapping.keys()))
    retval = []
    for testable in self.testables:
        missing = frozenset(x.filename for x in testable.file_verifiers if 
            not x.optional) - valid_files
        if missing:
            results._missing_to_testable_ids.setdefault(missing, set()).add(
                testable.id)
        elif testable.file_verifiers:
            retval.append(testable)
    if update:
        submission.test_case_results = []
        submission.testable_results = []
        submission.verification_results = results
        submission.verified_at = func.now()
    return retval