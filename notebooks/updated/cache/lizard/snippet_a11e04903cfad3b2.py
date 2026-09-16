def insert_text_to(cursor, text, fmt):
    while True:
        index = text.find(chr(8))
        if index == -1:
            break
        cursor.insertText(text[:index], fmt)
        if cursor.positionInBlock() > 0:
            cursor.deletePreviousChar()
        text = text[index + 1:]
    cursor.insertText(text, fmt)