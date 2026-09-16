def buildType(valtype, extra=[]):
    assert valtype[:1] == 'a', 'valtype must be an array'
    return Type(id='epics:nt/NTMultiChannel:1.0', spec=[('value', valtype),
        ('channelName', 'as'), ('descriptor', 's'), ('alarm', alarm), (
        'timeStamp', timeStamp), ('severity', 'ai'), ('status', 'ai'), (
        'message', 'as'), ('secondsPastEpoch', 'al'), ('nanoseconds', 'ai'),
        ('userTag', 'ai'), ('isConnected', 'a?')] + extra)