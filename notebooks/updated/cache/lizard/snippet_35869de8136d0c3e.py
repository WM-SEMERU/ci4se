def i2le_script(number):
    if number == 0:
        return '00'
    for i in range(80):
        try:
            return number.to_bytes(length=i, byteorder='little', signed=True
                ).hex()
        except Exception:
            continue