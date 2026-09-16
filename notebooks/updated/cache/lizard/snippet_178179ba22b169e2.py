def countries(instance):
    if instance['type'
        ] == 'location' and 'country' in instance and not instance['country'
        ].upper() in enums.COUNTRY_CODES:
        return JSONError(
            'Location `country` should be a valid ISO 3166-1 ALPHA-2 Code.',
            instance['id'], 'marking-definition-type')