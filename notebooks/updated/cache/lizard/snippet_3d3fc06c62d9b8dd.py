def calculate_checksum(source_string):
    countTo = int(len(source_string) / 2) * 2
    sum = 0
    count = 0
    loByte = 0
    hiByte = 0
    while count < countTo:
        if sys.byteorder == 'little':
            loByte = source_string[count]
            hiByte = source_string[count + 1]
        else:
            loByte = source_string[count + 1]
            hiByte = source_string[count]
        sum = sum + (ord(hiByte) * 256 + ord(loByte))
        count += 2
    if countTo < len(source_string):
        loByte = source_string[len(source_string) - 1]
        sum += ord(loByte)
    sum &= 4294967295
    sum = (sum >> 16) + (sum & 65535)
    sum += sum >> 16
    answer = ~sum & 65535
    answer = socket.htons(answer)
    return answer