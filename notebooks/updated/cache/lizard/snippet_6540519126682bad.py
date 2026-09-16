def GetPackages(classification, visibility):
    r = clc.v1.API.Call('post', 'Blueprint/GetPackages', {'Classification':
        Blueprint.classification_stoi[classification], 'Visibility':
        Blueprint.visibility_stoi[visibility]})
    if int(r['StatusCode']) == 0:
        return r['Packages']