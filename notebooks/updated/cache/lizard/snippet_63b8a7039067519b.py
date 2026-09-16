def report(zap_helper, output, output_format):
    if output_format == 'html':
        zap_helper.html_report(output)
    elif output_format == 'md':
        zap_helper.md_report(output)
    else:
        zap_helper.xml_report(output)
    console.info('Report saved to "{0}"'.format(output))