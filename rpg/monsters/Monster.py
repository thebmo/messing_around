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

    def take_damage(self, damage):
        self.hp -= damage
