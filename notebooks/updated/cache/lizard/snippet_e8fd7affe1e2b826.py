def validate_answer(self, value):
    try:
        serialized = json.dumps(value)
    except (ValueError, TypeError):
        raise serializers.ValidationError(
            'Answer value must be JSON-serializable')
    if len(serialized) > Submission.MAXSIZE:
        raise serializers.ValidationError('Maximum answer size exceeded.')
    return value