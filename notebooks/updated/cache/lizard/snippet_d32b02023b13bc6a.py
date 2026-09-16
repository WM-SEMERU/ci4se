def action_checklist_extractor(impact_report, component_metadata):
    context = {}
    provenance = impact_report.impact_function.provenance
    extra_args = component_metadata.extra_args
    context['component_key'] = component_metadata.key
    context['header'] = resolve_from_dictionary(extra_args, 'header')
    context['items'] = provenance['action_checklist']
    return context