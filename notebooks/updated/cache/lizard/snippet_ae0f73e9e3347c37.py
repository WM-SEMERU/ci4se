def routeByMonthAbbr(self, request, year, monthAbbr):
    month = DatePictures['Mon'].index(monthAbbr.lower()) // 4 + 1
    return self.serveMonth(request, year, month)