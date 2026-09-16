def sharedcontent_exists(slug):
    from django.contrib.sites.models import Site
    from fluent_contents.plugins.sharedcontent.models import SharedContent
    site = Site.objects.get_current()
    return SharedContent.objects.parent_site(site).filter(slug=slug).exists()