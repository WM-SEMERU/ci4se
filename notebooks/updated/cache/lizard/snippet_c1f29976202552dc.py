def save(self, *args, **kwargs):
    from organizations.exceptions import OrganizationMismatch
    if self.organization_user.organization.pk != self.organization.pk:
        raise OrganizationMismatch
    else:
        super(AbstractBaseOrganizationOwner, self).save(*args, **kwargs)