def answer_callback_query(self, callback_query_id: str, text: str=None,
    show_alert: bool=None, url: str=None, cache_time: int=0):
    return self.send(functions.messages.SetBotCallbackAnswer(query_id=int(
        callback_query_id), cache_time=cache_time, alert=show_alert or None,
        message=text, url=url))