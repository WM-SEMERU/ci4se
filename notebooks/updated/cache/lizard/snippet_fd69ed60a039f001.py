def process_rst_and_summaries(content_generators):
    for generator in content_generators:
        if isinstance(generator, generators.ArticlesGenerator):
            for article in (generator.articles + generator.translations +
                generator.drafts):
                rst_add_mathjax(article)
                if process_summary.mathjax_script is not None:
                    process_summary(article)
        elif isinstance(generator, generators.PagesGenerator):
            for page in generator.pages:
                rst_add_mathjax(page)
            for page in generator.hidden_pages:
                rst_add_mathjax(page)