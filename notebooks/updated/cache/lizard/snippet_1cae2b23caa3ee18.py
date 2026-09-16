def simxUnpackInts(intsPackedInString):
    b = []
    for i in range(int(len(intsPackedInString) / 4)):
        b.append(struct.unpack('<i', intsPackedInString[4 * i:4 * (i + 1)])[0])
    return b