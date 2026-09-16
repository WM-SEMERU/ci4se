def page_count(self):
    postcount = self.post_set.count()
    max_pages = postcount / get_paginate_by()
    if postcount % get_paginate_by() != 0:
        max_pages += 1
    return max_pages