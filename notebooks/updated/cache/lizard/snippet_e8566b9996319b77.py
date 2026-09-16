def network_profiles(self, obj):
    profile_name_list = self.network_profile_name_list(obj)
    profile_list = []
    for profile_name in profile_name_list:
        profile = Profile()
        flags = DWORD()
        access = DWORD()
        xml = LPWSTR()
        self._wlan_get_profile(self._handle, obj['guid'], profile_name,
            byref(xml), byref(flags), byref(access))
        profile.ssid = re.search('<name>(.*)</name>', xml.value).group(1)
        auth = re.search('<authentication>(.*)</authentication>', xml.value
            ).group(1).upper()
        profile.akm = []
        if auth not in akm_str_to_value_dict:
            if auth not in auth_str_to_value_dict:
                profile.auth = AUTH_ALG_OPEN
            else:
                profile.auth = auth_str_to_value_dict[auth]
                profile.akm.append(AKM_TYPE_NONE)
        else:
            profile.auth = AUTH_ALG_OPEN
            profile.akm.append(akm_str_to_value_dict[auth])
        profile_list.append(profile)
    return profile_list