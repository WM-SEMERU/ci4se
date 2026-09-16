async def dump_message(self, msg, msg_type=None):
    mtype = msg.__class__ if msg_type is None else msg_type
    fields = mtype.f_specs()
    for field in fields:
        await self.message_field(msg=msg, field=field)