def get_profile_location(tweet):
    if is_original_format(tweet):
        try:
            return tweet['user']['derived']['locations'][0]
        except KeyError:
            return None
    else:
        try:
            location = tweet['gnip']['profileLocations'][0]
            reconstructed_original_format = {}
            if location['address'].get('country', None) is not None:
                reconstructed_original_format['country'] = location['address'][
                    'country']
            if location['address'].get('countryCode', None) is not None:
                reconstructed_original_format['country_code'] = location[
                    'address']['countryCode']
            if location['address'].get('locality', None) is not None:
                reconstructed_original_format['locality'] = location['address'
                    ]['locality']
            if location['address'].get('region', None) is not None:
                reconstructed_original_format['region'] = location['address'][
                    'region']
            if location['address'].get('subRegion', None) is not None:
                reconstructed_original_format['sub_region'] = location[
                    'address']['subRegion']
            if location.get('displayName', None) is not None:
                reconstructed_original_format['full_name'] = location[
                    'displayName']
            if location.get('geo', None) is not None:
                reconstructed_original_format['geo'] = location['geo']
            return reconstructed_original_format
        except KeyError:
            return None