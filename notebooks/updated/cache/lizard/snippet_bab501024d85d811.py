def day_publications_card(date):
    d = date.strftime(app_settings.DATE_FORMAT)
    card_title = 'Reading on {}'.format(d)
    return {'card_title': card_title, 'publication_list': day_publications(
        date=date)}