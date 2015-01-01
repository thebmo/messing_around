from monster import Monster


class Slime(Monster):

    def __init__(
        self,
        name='Slime',
        hp=5,
        level=1,
        stats='AGI',
        is_dead=False,
        HLevel=0,
        ):
        
        self.name = name
        self.hp = int(hp + (.5 * HLevel))
        self.level = level + HLevel
        self.stats = stats
        self.is_dead = is_dead