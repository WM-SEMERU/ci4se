def viewTemplate(id):
    conn = Qubole.agent()
    return conn.get(Template.element_path(id))