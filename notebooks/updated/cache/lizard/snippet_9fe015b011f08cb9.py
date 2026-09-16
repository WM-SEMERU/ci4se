def get_all_tags_of_reminder(self, reminder_id):
    return self._iterate_through_pages(get_function=self.
        get_tags_of_reminder_per_page, resource=REMINDER_TAGS, **{
        'reminder_id': reminder_id})