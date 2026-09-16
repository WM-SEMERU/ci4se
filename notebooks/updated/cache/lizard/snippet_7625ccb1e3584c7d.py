def notify_for_new_version(self):
    try:
        recommend_update = False
        update_check_resp = requests.get(self.update_info_url, timeout=3)
        web_version = update_check_resp.json()['info']['version']
        api_logger.debug('RETRIEVED_VERSION: %s', web_version)
        available_version = SDK_BUILD_REGEX.search(web_version).groupdict()
        current_version = SDK_BUILD_REGEX.search(self.version).groupdict()
        available_major = available_version.get('major')
        available_minor = available_version.get('minor')
        available_patch = available_version.get('patch')
        available_build = available_version.get('build')
        current_major = current_version.get('major')
        current_minor = current_version.get('minor')
        current_patch = current_version.get('patch')
        current_build = current_version.get('build')
        api_logger.debug('AVAILABLE_VERSION: %s', available_version)
        api_logger.debug('CURRENT_VERSION: %s', current_version)
        if available_major > current_major:
            recommend_update = True
        elif available_major >= current_major and available_minor > current_minor:
            recommend_update = True
        elif available_major >= current_major and available_minor >= current_minor and available_patch > current_patch:
            recommend_update = True
        api_logger.debug('NEED_UPDATE: %s', recommend_update)
        if recommend_update:
            sys.stderr.write(
                """WARNING: CloudGenix Python SDK upgrade available. SDKs are typically deprecated 6 months after release of a new version.
	Latest Version: {0}
	Current Version: {1}
	For more info, see 'https://github.com/cloudgenix/sdk-python'. Additionally, this message can be suppressed by instantiating the API with API(update_check=False).

"""
                .format(web_version, self.version))
        return
    except Exception:
        return