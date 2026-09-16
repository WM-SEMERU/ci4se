def badge_form(model):


    class BadgeForm(ModelForm):
        model_class = Badge
        kind = fields.RadioField(_('Kind'), [validators.DataRequired()],
            choices=model.__badges__.items(), description=_(
            'Kind of badge (certified, etc)'))
    return BadgeForm