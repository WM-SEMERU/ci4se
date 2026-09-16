def get(self):
    environment_variables_output = [html_for_env_var(key) for key in sorted
        (os.environ)]
    cgi_arguments_output = []
    if os.getenv('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
        form = cgi.FieldStorage()
        if not form:
            cgi_arguments_output.append('No CGI arguments given...')
        else:
            for cgi_argument in form:
                cgi_arguments_output.append(html_for_cgi_argument(
                    cgi_argument, form))
    else:
        data = ''
        cgi_arguments_output.append(STDIN_TEMPLATE.format(len(data)))
        cgi_arguments_output.append(cgi.escape(data))
    modules_api_output = [html_for_modules_method('get_current_module_name'
        ), html_for_modules_method('get_current_version_name'),
        html_for_modules_method('get_current_instance_id'),
        html_for_modules_method('get_modules'), html_for_modules_method(
        'get_versions'), html_for_modules_method('get_default_version'),
        html_for_modules_method('get_hostname')]
    result = PAGE_TEMPLATE.format(users.CreateLoginURL(self.request.url),
        users.CreateLogoutURL(self.request.url), '<br>\n'.join(
        environment_variables_output), '<br>\n'.join(cgi_arguments_output),
        '<br>\n'.join(modules_api_output))
    self.response.write(result)