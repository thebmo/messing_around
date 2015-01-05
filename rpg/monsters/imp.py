from monster import Monster


class Imp(Monster):

    def __init__(
        self,
        name='Imp',
        max_hp=6,
        max_ap=1,
        level=1,
        is_dead=False,
        exp=2,
        damage=2
        ):

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_ap = max_ap
        self.ap = max_ap
        self.level = level
        self.is_dead = is_dead
        self.exp = exp
        self.damage = damage
