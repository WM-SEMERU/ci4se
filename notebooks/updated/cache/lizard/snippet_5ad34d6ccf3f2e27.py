def execute_console_command(frame, thread_id, frame_id, line, buffer_output
    =True):
    console_message = ConsoleMessage()
    interpreter = get_interactive_console(thread_id, frame_id, frame,
        console_message)
    more, output_messages, error_messages = interpreter.push(line, frame,
        buffer_output)
    console_message.update_more(more)
    for message in output_messages:
        console_message.add_console_message(CONSOLE_OUTPUT, message)
    for message in error_messages:
        console_message.add_console_message(CONSOLE_ERROR, message)
    return console_message