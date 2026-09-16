def _GetOutputModulesInformation(self):
    output_modules_information = []
    for name, output_class in output_manager.OutputManager.GetOutputClasses():
        output_modules_information.append((name, output_class.DESCRIPTION))
    return output_modules_information