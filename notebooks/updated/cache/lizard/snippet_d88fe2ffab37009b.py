def static(ctx, slot, password, generate, length, keyboard_layout, no_enter,
    force):
    controller = ctx.obj['controller']
    keyboard_layout = KEYBOARD_LAYOUT[keyboard_layout]
    if password and len(password) > 38:
        ctx.fail('Password too long (maximum length is 38 characters).')
    if generate and not length:
        ctx.fail('Provide a length for the generated password.')
    if not password and not generate:
        password = click.prompt('Enter a static password', err=True)
    elif not password and generate:
        password = generate_static_pw(length, keyboard_layout)
    if not force:
        _confirm_slot_overwrite(controller, slot)
    try:
        controller.program_static(slot, password, not no_enter,
            keyboard_layout=keyboard_layout)
    except YkpersError as e:
        _failed_to_write_msg(ctx, e)