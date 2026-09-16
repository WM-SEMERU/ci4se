def search_results_total(html, xpath, check, delimiter):
    for container in html.findall(xpath):
        if check in container.findtext('.'):
            text = container.findtext('.').split(delimiter)
            total = int(text[-1].strip())
            return total