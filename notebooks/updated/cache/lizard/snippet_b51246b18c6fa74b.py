def get_skyline(lrh):
    skyline, live = [], []
    i, n = 0, len(lrh)
    while i < n or live:
        if not live or i < n and lrh[i][0] <= -live[0][1]:
            x = lrh[i][0]
            while i < n and lrh[i][0] == x:
                heapq.heappush(live, (-lrh[i][2], -lrh[i][1]))
                i += 1
        else:
            x = -live[0][1]
            while live and -live[0][1] <= x:
                heapq.heappop(live)
        height = len(live) and -live[0][0]
        if not skyline or height != skyline[-1][1]:
            skyline += [x, height],
    return skyline