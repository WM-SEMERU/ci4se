def _deserialize(self, value, attr, data):
    token_builder = URLSafeTimedSerializer(current_app.config['SECRET_KEY'],
        salt=data['verb'])
    result = token_builder.loads(value, max_age=current_app.config[
        'OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME'])
    result['token'] = value
    result['kwargs'] = self.root.load(result['kwargs'], partial=True).data
    return result