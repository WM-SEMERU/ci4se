def get_comment_ids_by_books(self, book_ids):
    id_list = []
    for comment in self.get_comments_by_books(book_ids):
        id_list.append(comment.get_id())
    return IdList(id_list)