from character import *
from coord import *


class Villain(Character):
    def __init__(self):
        super().__init__(Player.VILLAIN)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if 0 < to_coord.x - from_coord.x <= self.move or 0 < to_coord.y - from_coord.y <= self.move:
            return False
        
        super().is_valid_move(from_coord, to_coord, board)


    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, attack=True, lst: list = [], *args, **kwargs) -> int:
        super().calculate_dice(attack, lst, *args, **kwargs)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        super().deal_damage(target, damage, *args, **kwargs)

    def __str__(self) -> str:
        super().__str__()

class Goblin(Villain):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]

class Necromancer(Villain):
    def __init__(self):
        super().__init__()
        self.combat = [2, 1]
        self.range = 3

    # def raise_dead(self, target: Character):
    #     if target in range
    #         target.player = Player.VILLAIN
    #         target.player.temp_health = target.player.health // 2

class Skeleton(Villain):
    def __init__(self):
        super().__init__()
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2


class Hero(Character, ABC):
    def __init__(self):
        super().__init__(Player.HERO)

class Paladin(Hero, ABC):
    pass

class Mage(Hero, ABC):
    pass

class Warrior(Hero, ABC):
    pass

class Ranger(Hero, ABC):
    pass
