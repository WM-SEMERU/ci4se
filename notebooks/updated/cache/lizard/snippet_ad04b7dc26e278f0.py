def _check_branch(self, revision, branch):
    clog_url = self.hg_url / branch / 'json-log' / revision
    try:
        Log.note('Searching through changelog {{url}}', url=clog_url)
        clog_obj = http.get_json(clog_url, retry=RETRY)
        if isinstance(clog_obj, (text_type, str)):
            Log.note(
                'Revision {{cset}} does not exist in the {{branch}} branch',
                cset=revision, branch=branch)
            return False
    except Exception as e:
        Log.note('Unexpected error getting changset-log for {{url}}: {{error}}'
            , url=clog_url, error=e)
        return False
    return True