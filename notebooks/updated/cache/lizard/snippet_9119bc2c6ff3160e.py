def MakeDeployableBinary(self, template_path, output_path):
    context = self.context + ['Client Context']
    zip_data = io.BytesIO()
    output_zip = zipfile.ZipFile(zip_data, mode='w', compression=zipfile.
        ZIP_DEFLATED)
    z_template = zipfile.ZipFile(open(template_path, 'rb'))
    completed_files = ['grr-client.exe', 'GRRservice.exe',
        'dbg_grr-client.exe', 'dbg_GRRservice.exe']
    client_bin_name = config.CONFIG.Get('Client.binary_name', context=context)
    console_build = config.CONFIG.Get('ClientBuilder.console', context=context)
    if console_build:
        client_filename = 'dbg_grr-client.exe'
        service_filename = 'dbg_GRRservice.exe'
    else:
        client_filename = 'grr-client.exe'
        service_filename = 'GRRservice.exe'
    bin_name = z_template.getinfo(client_filename)
    output_zip.writestr(client_bin_name, z_template.read(bin_name))
    CopyFileInZip(z_template, 'grr-client.exe.manifest', output_zip, 
        '%s.manifest' % client_bin_name)
    completed_files.append('grr-client.exe.manifest')
    service_template = z_template.getinfo(service_filename)
    service_bin_name = config.CONFIG.Get('Nanny.service_binary_name',
        context=context)
    output_zip.writestr(service_bin_name, z_template.read(service_template))
    if config.CONFIG['Client.fleetspeak_enabled']:
        self._GenerateFleetspeakServiceConfig(output_zip)
    if self.signed_template:
        CreateNewZipWithSignedLibs(z_template, output_zip, ignore_files=
            completed_files)
    else:
        CreateNewZipWithSignedLibs(z_template, output_zip, ignore_files=
            completed_files, signer=self.signer)
    output_zip.close()
    return self.MakeSelfExtractingZip(zip_data.getvalue(), output_path)