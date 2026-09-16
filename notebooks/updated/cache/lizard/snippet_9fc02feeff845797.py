def checkUserManage(worksheet, request, redirect=True):
    allowed = worksheet.checkUserManage()
    if allowed == False and redirect == True:
        destination_url = worksheet.absolute_url() + '/manage_results'
        request.response.redirect(destination_url)