def clean_timestamp(self):
    ts = self.cleaned_data['timestamp']
    if time.time() - ts > 2 * 60 * 60:
        raise forms.ValidationError('Timestamp check failed')
    return ts