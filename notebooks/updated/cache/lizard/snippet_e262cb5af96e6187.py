def client_mechanisms(self):
    return [mech for mech in self.mechs.values() if isinstance(mech,
        ClientMechanism)]