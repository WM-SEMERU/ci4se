def generate_html(store):
    spline = {'version': VERSION, 'url':
        'https://github.com/Nachtfeuer/pipeline', 'generated': datetime.now
        ().strftime('%A, %d. %B %Y - %I:%M:%S %p')}
    html_template_file = os.path.join(os.path.dirname(__file__),
        'templates/report.html.j2')
    with open(html_template_file) as handle:
        html_template = handle.read()
        return render(html_template, spline=spline, store=store)