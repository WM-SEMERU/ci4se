def send_message(chat_id):
    files = request.files
    if files:
        res = send_media(chat_id, request)
    else:
        message = request.form.get('message')
        res = g.driver.chat_send_message(chat_id, message)
    if res:
        return jsonify(res)
    else:
        return False