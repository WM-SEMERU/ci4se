async def edit_message(self, entity, message=None, text=None, *, parse_mode
    =(), link_preview=True, file=None, buttons=None):
    if isinstance(entity, types.InputBotInlineMessageID):
        text = message
        message = entity
    elif isinstance(entity, types.Message):
        text = message
        message = entity
        entity = entity.to_id
    text, msg_entities = await self._parse_message_text(text, parse_mode)
    file_handle, media, image = await self._file_to_media(file)
    if isinstance(entity, types.InputBotInlineMessageID):
        return await self(functions.messages.EditInlineBotMessageRequest(id
            =entity, message=text, no_webpage=not link_preview, entities=
            msg_entities, media=media, reply_markup=self.build_reply_markup
            (buttons)))
    entity = await self.get_input_entity(entity)
    request = functions.messages.EditMessageRequest(peer=entity, id=utils.
        get_message_id(message), message=text, no_webpage=not link_preview,
        entities=msg_entities, media=media, reply_markup=self.
        build_reply_markup(buttons))
    msg = self._get_response_message(request, await self(request), entity)
    await self._cache_media(msg, file, file_handle, image=image)
    return msg