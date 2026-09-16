def about_box():
    about_info = wx.adv.AboutDialogInfo()
    for k, v in metadata.items():
        setattr(about_info, snake2ucamel(k), v)
    wx.adv.AboutBox(about_info)