def attach_translated_content(self, local_main_lang_page, content, locale):
    try:
        page = self.attach_page(local_main_lang_page.get_parent(), content)
    except:
        return None
    try:
        language = SiteLanguageRelation.objects.get(language_setting=self.
            language_setting, locale=locale)
        page.language = language
        page.translated_pages.add(local_main_lang_page)
        local_main_lang_page.translated_pages.add(page)
        page.save()
        local_main_lang_page.save()
    except:
        page.delete()
    return page