def render_to_response(self, context, *args, **kwargs):
    preview_outputs = []
    file_outputs = []
    bast_ctx = context
    added = set()
    for output_group, output_files in context['job_info']['file_groups'].items(
        ):
        for output_file_content in output_files:
            if output_group:
                bast_ctx.update({'job_info': context['job_info'],
                    'output_group': output_group, 'output_file_content':
                    output_file_content})
                preview = render_to_string('wooey/preview/%s.html' %
                    output_group, bast_ctx)
                preview_outputs.append(preview)
    for file_info in context['job_info']['all_files']:
        if file_info and file_info.get('name') not in added:
            row_ctx = dict(file=file_info, **context)
            table_row = render_to_string('wooey/jobs/results/table_row.html',
                row_ctx)
            file_outputs.append(table_row)
            added.add(file_info.get('name'))
    return JsonResponse({'status': context['job_info']['status'].lower(),
        'command': context['job_info']['job'].command, 'stdout': context[
        'job_info']['job'].get_stdout(), 'stderr': context['job_info'][
        'job'].get_stderr(), 'preview_outputs_html': preview_outputs,
        'file_outputs_html': file_outputs})