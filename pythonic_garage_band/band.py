class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician(Band):
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.role} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"


class Guitarist(Musician):
    def __init__(self, name, instrument="guitar", role="Guitarist" ):
        self.name = name
        self.instrument = instrument
        self.role = role

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name, instrument = "bass", role="Bassist" ):
        self.name = name
        self.instrument = instrument
        self.role = role

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name, instrument = "drums", role = "Drummer" ):
        self.name = name
        self.instrument = instrument
        self.role = role

    def play_solo(self):
        return "rattle boom crash"
