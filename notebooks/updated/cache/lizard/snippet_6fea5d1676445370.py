def calc_contriarea_v1(self):
    con = self.parameters.control.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    sta = self.sequences.states.fastaccess
    if con.resparea and der.relsoilarea > 0.0:
        flu.contriarea = 0.0
        for k in range(con.nmbzones):
            if con.zonetype[k] in (FIELD, FOREST):
                if con.fc[k] > 0.0:
                    flu.contriarea += der.relsoilzonearea[k] * (sta.sm[k] /
                        con.fc[k]) ** con.beta[k]
                else:
                    flu.contriarea += der.relsoilzonearea[k]
    else:
        flu.contriarea = 1.0