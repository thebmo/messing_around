from monster import Monster


class Slime(Monster):

    def __init__(
        self,
        name='Slime',
        max_hp=5,
        max_ap=0,
        level=1,
        is_dead=False,
        exp=1,
        damage=1
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
