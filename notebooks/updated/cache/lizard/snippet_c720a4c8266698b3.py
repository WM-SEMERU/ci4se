async def recv(self):
    pts, time_base = await self.next_timestamp()
    frame = VideoFrame(width=640, height=480)
    for p in frame.planes:
        p.update(bytes(p.buffer_size))
    frame.pts = pts
    frame.time_base = time_base
    return frame