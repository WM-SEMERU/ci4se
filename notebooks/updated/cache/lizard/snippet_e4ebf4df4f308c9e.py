def save_account(message, collection=DATABASE.account):
    try:
        collection.create_index([('account_cookie', ASCENDING), (
            'user_cookie', ASCENDING), ('portfolio_cookie', ASCENDING)],
            unique=True)
    except:
        pass
    collection.update({'account_cookie': message['account_cookie'],
        'portfolio_cookie': message['portfolio_cookie'], 'user_cookie':
        message['user_cookie']}, {'$set': message}, upsert=True)