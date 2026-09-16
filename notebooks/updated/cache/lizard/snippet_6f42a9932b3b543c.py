def inserir(self, id_equipment, id_script):
    equipment_script_map = dict()
    equipment_script_map['id_equipment'] = id_equipment
    equipment_script_map['id_script'] = id_script
    code, xml = self.submit({'equipment_script': equipment_script_map},
        'POST', 'equipmentscript/')
    return self.response(code, xml)