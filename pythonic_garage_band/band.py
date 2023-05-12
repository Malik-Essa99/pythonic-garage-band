class Musician:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    
class Band:
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    
    instances = []
    def __init__(self,name,members):
        self.name = name
        self.members = members
        self.__class__.instances.append(self)
    
    def play_solos(self):
        lst_play_solos = []
        for member in self.members:
            lst_play_solos.append(member.play_solo())
        return lst_play_solos
    
    @classmethod
    def to_list(cls):
        return cls.instances
    

class Guitarist(Musician):

    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
    
if __name__ == '__main__':
    pass
    
