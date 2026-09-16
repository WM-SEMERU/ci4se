def breeding_female_location_type(self):
    try:
        self.breeding_females.all()[0].Cage
        if int(self.breeding_females.all()[0].Cage) == int(self.Cage):
            type = 'resident-breeder'
        else:
            type = 'non-resident-breeder'
    except IndexError:
        type = 'unknown-breeder'
    except ValueError:
        type = 'unknown-breeder'
    return type