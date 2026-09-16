def detach_zone(organization_id_or_slug):
    organization = Organization.objects.get_by_id_or_slug(
        organization_id_or_slug)
    if not organization:
        exit_with_error('No organization found for {0}'.format(
            organization_id_or_slug))
    log.info('Detaching {organization} from {organization.zone}'.format(
        organization=organization))
    organization.zone = None
    organization.save()
    log.info('Done')