async def message_handler(self, event):
    chat = await event.get_chat()
    if event.is_group:
        if event.out:
            sprint('>> sent "{}" to chat {}'.format(event.text,
                get_display_name(chat)))
        else:
            sprint('<< {} @ {} sent "{}"'.format(get_display_name(await
                event.get_sender()), get_display_name(chat), event.text))
    elif event.out:
        sprint('>> "{}" to user {}'.format(event.text, get_display_name(chat)))
    else:
        sprint('<< {} sent "{}"'.format(get_display_name(chat), event.text))