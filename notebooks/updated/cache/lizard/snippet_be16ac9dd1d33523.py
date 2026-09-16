def view(self, rec):
    out_json = {'uid': rec.uid, 'time_update': rec.time_update, 'title':
        rec.title, 'cnt_html': tornado.escape.xhtml_unescape(rec.cnt_html)}
    self.write(json.dumps(out_json))