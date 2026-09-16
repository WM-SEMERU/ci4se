def list_to_csv_response(data, title='report', header=None, widths=None):
    response = HttpResponse(content_type='text/csv; charset=UTF-8')
    cw = csv.writer(response)
    for row in chain([header] if header else [], data):
        cw.writerow([force_text(s).encode(response.charset) for s in row])
    return response