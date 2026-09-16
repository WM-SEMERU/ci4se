def a_message_callback(ctx):
    message = ctx.ctrl.after.strip().splitlines()[-1]
    ctx.device.chain.connection.emit_message(message, log_level=logging.INFO)
    return True