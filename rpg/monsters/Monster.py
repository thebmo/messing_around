class Monster(object):
    """
        basic moster class
    """


    def __init__(
        self,
        name='Juju',
        max_hp=99999,
        max_ap=999,
        level=99,
        is_dead=False,
        exp=0,
        damage=999
        ):

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_ap = max_ap
        self.ap = max_ap
        self.level = level
        self.stats = stats
        self.is_dead = is_dead
        self.exp = exp
        self.damage=damage


    def __str__(self):
        return self.name


    def __ref__(self):
        return self.name


    def take_damage(self, taken_damage):
        self.hp -= taken_damage
        if self.hp < 1:
            self.is_dead = True


    def deal_damage(self):
        return self.damage
        