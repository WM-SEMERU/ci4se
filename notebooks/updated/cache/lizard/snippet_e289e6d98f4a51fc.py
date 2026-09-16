def roll(self, value):
    if type(value) != str:
        raise TypeError('Dice roll must be a string in dice notation')
    try:
        roll_dice(value)
    except Exception as e:
        raise ValueError(
            'Dice roll specified was not a valid diceroll.\n%s\n' % str(e))
    else:
        self._roll = value