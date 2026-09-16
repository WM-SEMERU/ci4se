def parse_failed_targets(test_registry, junit_xml_path, error_handler):
    failed_targets = defaultdict(set)

    def parse_junit_xml_file(path):
        try:
            xml = XmlParser.from_file(path)
            failures = int(xml.get_attribute('testsuite', 'failures'))
            errors = int(xml.get_attribute('testsuite', 'errors'))
            if failures or errors:
                for testcase in xml.parsed.getElementsByTagName('testcase'):
                    test_failed = testcase.getElementsByTagName('failure')
                    test_errored = testcase.getElementsByTagName('error')
                    if test_failed or test_errored:
                        test = Test(classname=testcase.getAttribute(
                            'classname'), methodname=testcase.getAttribute(
                            'name'))
                        target = test_registry.get_owning_target(test)
                        failed_targets[target].add(test)
        except (XmlParser.XmlError, ValueError) as e:
            error_handler(ParseError(path, e))
    if os.path.isdir(junit_xml_path):
        for root, _, files in safe_walk(junit_xml_path):
            for junit_xml_file in fnmatch.filter(files, 'TEST-*.xml'):
                parse_junit_xml_file(os.path.join(root, junit_xml_file))
    else:
        parse_junit_xml_file(junit_xml_path)
    return dict(failed_targets)