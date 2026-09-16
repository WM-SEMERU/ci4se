def get_number_of_atoms(self):
    strc = self.get_output_structure()
    if not strc:
        return None
    return Property(scalars=[Scalar(value=len(strc))], units='/unit cell')