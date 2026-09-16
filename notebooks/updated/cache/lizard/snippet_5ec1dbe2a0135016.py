async def clear_topic_channel(self, channel):
    try:
        if self.topicchannel:
            await client.edit_channel(self.topicchannel, topic='')
    except Exception as e:
        logger.exception(e)
    self.topicchannel = None
    logger.debug('Clearing topic channel')
    data = datatools.get_data()
    data['discord']['servers'][self.server_id][_data.modulename]['topic_id'
        ] = ''
    datatools.write_data(data)
    await client.send_typing(channel)
    embed = ui_embed.topic_update(channel, self.topicchannel)
    await embed.send()