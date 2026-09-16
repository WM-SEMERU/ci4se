def html2data(html_string):
    spans = extract_spans(html_string)
    column_count = get_html_column_count(html_string)
    row_count = get_html_row_count(spans)
    count = 0
    while count < len(spans):
        if len(spans[count]) == 1:
            spans.pop(count)
        else:
            count += 1
    table = extract_table(html_string, row_count, column_count)
    use_headers = headers_present(html_string)
    return table, spans, use_headers