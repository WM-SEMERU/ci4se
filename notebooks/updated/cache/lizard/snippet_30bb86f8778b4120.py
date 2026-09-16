def reactToAMQPMessage(message, send_back):
    if _instanceof(message, structures.ScanFile):
        result = antivirus.save_and_scan(message.filename, message.b64_data)
        return structures.ScanResult(message.filename, result)
    elif _instanceof(message, structures.UpdateDatabase):
        return structures.DatabaseUpdated(antivirus.update_database())
    raise ValueError("Unknown type of request: '" + str(type(message)) + "'!")