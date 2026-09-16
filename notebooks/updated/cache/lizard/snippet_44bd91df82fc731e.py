def generate_html():
    html_file = open(html_filename, 'w')
    html_file.write('<html><body>')
    html_file.write('<h1>Here are some graphs for you!</h1>')
    for image in [lines_filename, bars_filename, histogram_filename]:
        html_file.write("<div><h2>{0}</h2><img src='{0}' /></div>".format(
            image))
    html_file.write('</body></html>')
    html_file.close()