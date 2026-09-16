def runTemplate(id, data={}):
    conn = Qubole.agent()
    path = str(id) + '/run'
    res = conn.post(Template.element_path(path), data)
    cmdType = res['command_type']
    cmdId = res['id']
    cmdClass = eval(cmdType)
    cmd = cmdClass.find(cmdId)
    while not Command.is_done(cmd.status):
        time.sleep(Qubole.poll_interval)
        cmd = cmdClass.find(cmd.id)
    return Template.getResult(cmdClass, cmd)