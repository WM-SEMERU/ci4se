def summary(self, html_partial=False):
    try:
        ruthless = True
        recallPriority = self.recallPriority
        if recallPriority:
            ruthless = False
            self.TEXT_LENGTH_THRESHOLD = 2
            self.RETRY_LENGTH = 25
        while True:
            self._html(True)
            for i in self.tags(self.html, 'script', 'style'):
                i.drop_tree()
            for i in self.tags(self.html, 'body'):
                i.set('id', 'readabilityBody')
            if ruthless:
                self.remove_unlikely_candidates()
            self.transform_misused_divs_into_paragraphs()
            candidates = self.score_paragraphs()
            best_candidates = self.select_best_candidates(candidates)
            if best_candidates and not recallPriority:
                article = self.get_article_from_candidates(candidates,
                    best_candidates, html_partial)
            elif ruthless and not recallPriority:
                log.debug('ruthless removal did not work. ')
                ruthless = False
                self.debug(
                    'ended up stripping too much - going for a safer _parse')
                continue
            else:
                log.debug(
                    'Ruthless and lenient parsing did not work. Returning raw html'
                    )
                article = self.html.find('body')
                if article is None:
                    article = self.html
            cleaned_article = self.sanitize(article, candidates)
            article_length = len(cleaned_article or '')
            retry_length = self.options.get('retry_length', self.RETRY_LENGTH)
            of_acceptable_length = article_length >= retry_length
            if ruthless and not of_acceptable_length:
                ruthless = False
                continue
            else:
                return cleaned_article
    except Exception as e:
        print('error: %s', e)
        log.exception('error getting summary: ')
        raise Exception(Unparseable(str(e)), None, sys.exc_info()[2])