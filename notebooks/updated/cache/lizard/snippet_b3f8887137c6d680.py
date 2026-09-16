def to_array(self):
    array = super(InlineKeyboardButton, self).to_array()
    array['text'] = u(self.text)
    if self.url is not None:
        array['url'] = u(self.url)
    if self.callback_data is not None:
        array['callback_data'] = u(self.callback_data)
    if self.switch_inline_query is not None:
        array['switch_inline_query'] = u(self.switch_inline_query)
    if self.switch_inline_query_current_chat is not None:
        array['switch_inline_query_current_chat'] = u(self.
            switch_inline_query_current_chat)
    if self.callback_game is not None:
        array['callback_game'] = self.callback_game.to_array()
    if self.pay is not None:
        array['pay'] = bool(self.pay)
    return array