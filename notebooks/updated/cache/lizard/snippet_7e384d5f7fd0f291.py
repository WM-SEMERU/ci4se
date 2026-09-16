def upload_as_zip(name, filename):
    location = list(IPList.objects.filter(name))
    if location:
        iplist = location[0]
        return iplist.upload(filename=filename)