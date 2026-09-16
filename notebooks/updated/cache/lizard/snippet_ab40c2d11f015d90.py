def polyline(self, arr):
    for i in range(0, len(arr) - 1):
        self.line(arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1])