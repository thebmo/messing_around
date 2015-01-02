class Monster(object):
    """
        basic moster class
    """


    def __init__(
        self,
        name='Juju',
        hp=5,
        level=1,
        stats='AGI',
        is_dead=False
        ):

        self.name = name
        self.hp = hp
        self.level = level
        self.stats = stats
        self.is_dead = is_dead


    def __str__(self):
        return self.name


    def __ref__(self):
        return self.name


    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 1:
            self.is_dead = True

