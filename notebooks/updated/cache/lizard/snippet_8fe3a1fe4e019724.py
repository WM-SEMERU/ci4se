def check_title_match(expected_title, pa11y_results, logger):
    if not pa11y_results:
        return
    title_errs = [err for err in pa11y_results if err['context'].startswith
        ('<title')]
    for err in title_errs:
        title_elmt = html.fragment_fromstring(err['context'])
        elided_title = title_elmt.text.strip()
        if elided_title.endswith('...'):
            pa11y_title = elided_title[0:-4].strip()
        else:
            pa11y_title = elided_title
        if pa11y_title not in expected_title:
            msg = (
                'Parser mismatch! Scrapy saw full title "{scrapy_title}", Pa11y saw elided title "{elided_title}".'
                .format(scrapy_title=expected_title, elided_title=elided_title)
                )
            logger.error(msg)