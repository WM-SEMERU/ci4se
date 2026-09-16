def _input_file_as_html_links(cls, session: AppSession):
    scrape_result = session.factory['HTMLScraper'].scrape_file(session.args
        .input_file, encoding=session.args.local_encoding or 'utf-8')
    for context in scrape_result.link_contexts:
        yield context.link