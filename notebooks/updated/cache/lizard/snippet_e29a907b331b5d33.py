def create_modeladmin(self, base_admin=admin.ModelAdmin):
    _builder = self


    class CustomFieldModelBaseAdmin(base_admin):

        def __init__(self, *args, **kwargs):
            super(CustomFieldModelBaseAdmin, self).__init__(*args, **kwargs)

        def save_model(self, request, obj, form, change):
            obj.save()
            if hasattr(form, 'save_custom_fields'):
                form.save_custom_fields()
    return CustomFieldModelBaseAdmin