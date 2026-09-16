def write_to_file(chats, chatfile):
    with open(chatfile, 'w') as handler:
        handler.write('\n'.join(str(id_) for id_ in chats))