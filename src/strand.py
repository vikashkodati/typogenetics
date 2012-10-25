import bases

class NotInSet(ValueError):
    pass

class NotAString(TypeError):
    pass

class Strand:
    """It's a sequence of units, occupied by bases.
    Simply speaking, string of 'ACGT'."""
    def __init__(self, string):
        if isinstance(string, str):
            if not frozenset(string).issubset(bases.bases):
                raise NotInSet
        else:
            raise NotAString

        self.units = string

    def __repr__(self):
        return 'Strand("{0}")'.format(self.units)

    def __str__(self):
        return 'Strand("{0}")'.format(self.units)
