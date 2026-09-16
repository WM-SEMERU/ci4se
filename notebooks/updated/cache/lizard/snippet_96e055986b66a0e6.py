def is_correctness_available(self, question_id):
    response = self.get_response(question_id)
    if response.is_answered():
        item = self._get_item(response.get_item_id())
        return item.is_correctness_available_for_response(response)
    return False