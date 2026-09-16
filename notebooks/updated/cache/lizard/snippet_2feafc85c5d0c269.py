def mail_sent_contains_html(self):
    for email in mail.outbox:
        try:
            html = next(content for content, mime in email.alternatives if 
                mime == 'text/html')
            dom1 = parse_html(html)
            dom2 = parse_html(self.multiline)
            assert_in(dom1, dom2)
        except AssertionError as exc:
            print('Email did not match', exc)
            continue
        return True
    raise AssertionError('No email contained the HTML')