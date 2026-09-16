def update_bookmark(self, old, new, *, max_retries=3):

    def replace_bookmark(bookmarks, old, new):
        modified_bookmarks = list(bookmarks)
        try:
            i = bookmarks.index(old)
            modified_bookmarks[i] = new
        except ValueError:
            modified_bookmarks.append(new)
        return modified_bookmarks
    with (yield from self._lock):
        bookmarks = yield from self._get_bookmarks()
        try:
            yield from self._set_bookmarks(replace_bookmark(bookmarks, old,
                new))
            retries = 0
            bookmarks = yield from self._get_bookmarks()
            while retries < max_retries:
                if new in bookmarks:
                    break
                yield from self._set_bookmarks(replace_bookmark(bookmarks,
                    old, new))
                bookmarks = yield from self._get_bookmarks()
                retries += 1
            if new not in bookmarks:
                raise RuntimeError('Cold not update bookmark')
        finally:
            self._diff_emit_update(bookmarks)