from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from enum import Enum
from random import randint
from coord import Coord

class CharacterDeath(Exception):

    def __init__(self, msg, char: Character):
        self.message = msg
        char.temp_health = 0


class InvalidAttack(Exception):
    pass


class Player(Enum):
    VILLAIN = 0
    HERO = 1

@abstractmethod
class Character(ABC):
    @abstractmethod
    def __init__(self, player: Player):
        self.__player = player
        self.__health = 5
        self.__temp_health = 5
        self.__attack = 3
        self.__defense = 3
        self.__move = 3
        self.__range = 1
        if self.__move and self.__range < 1:
            raise ValueError
        if self.__attack and self.__defense < 0:
            raise ValueError

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, new):
        if not isinstance(new, Player):
            raise TypeError
        self.__player = new

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, num: int):
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise ValueError
        self.__health = num

    @property
    def temp_health(self) -> int:
        return self.__temp_health

    @temp_health.setter
    def temp_health(self, num: int):
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise CharacterDeath(f"You have been killed by {self}!", self)
        self.__temp_health = num

    @property
    def combat(self) -> list:
        return [self.__attack, self.__defense]

    @combat.setter
    def combat(self, lst: list) -> None:
        if not isinstance(lst, list):
            raise TypeError
        if not isinstance(lst[0], int) and not isinstance(lst[1], int):
            raise TypeError
        if lst[0] < 0 and lst[1] < 0:
            raise ValueError
        self.__attack = lst[0]
        self.__defense = lst[1]


    @property
    def range(self) -> int:
        return self.__range

    @range.setter
    def range(self, num: int):
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise ValueError
        self.__range = num

    @property
    def move(self) -> int:
        if not isinstance(self.__move, int):
            if self.__move < 1:
                raise ValueError
            else:
                raise TypeError
        return self.__move

    @move.setter
    def move(self, num: int):
        if not isinstance(num, int):
            raise TypeError
        if num < 0 or num <= 0:
            raise ValueError
        self.__move = num

    @abstractmethod
    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if from_coord.x < 0 or from_coord.x >= len(board) or from_coord.y < 0 or from_coord.y >= len(board[-1]): # checks to make sure indexs we are in the proper range
            return False

        if to_coord.x < 0 or to_coord.x >= len(board) or to_coord.y < 0 or to_coord.y >= len(board[-1]):
            return False

        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:  # ensures that index from from_coord and to_cord aren't the same
            return False

        if board[from_coord.x][from_coord.y] != self:
            return False

        if board[to_coord.x][to_coord.y] is not None:  # ensures player is in the starting cord and ending cord is empty
            return False

        return True


    @abstractmethod
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if from_coord.x < 0 or from_coord.x >= len(board) or from_coord.y < 0 or from_coord.y >= len(board[-1]): # checks to make sure indexs we are in the proper range
            return False

        if to_coord.x < 0 or to_coord.x >= len(board) or to_coord.y < 0 or to_coord.y >= len(board[-1]):
            return False

        if from_coord.x == to_coord.x and from_coord.y == to_coord.y:  # ensures that index from from_coord and to_cord aren't the same
            return False

        if board[from_coord.x][from_coord.y] != self:
            return False

        if board[to_coord.x][to_coord.y] is None:  # ensures player is in the starting cord and ending cord is empty
            return False

        return True

    @abstractmethod
    def calculate_dice(self, attack=True, lst: list = [], *args, **kwargs) -> int:
        success = 0
        def_success = 0

        if attack == True:
            for i in range(self.combat[0] - 1):
                lst.append(randint(1, 6))
                for i in lst:
                    if i >= 4:
                        success += 1

        if attack == False:
            for i in range(self.combat[1] - 1):
                lst.append(randint(1, 6))
                for i in lst:
                    if i >= 3:
                        def_success += 1

        total = success - def_success
        return total



    @abstractmethod
    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        damage = target.temp_health - damage

        if damage <= 0:
            target.temp_health = damage
            raise CharacterDeath(f'{target} was {damage} damage!', target)
        else:
            target.temp_health = damage
            print(f'{target} was {damage} damage!')




    @abstractmethod
    def __str__(self) -> str:
       return self.__class__.__name__

class Player(Enum):
    VILLAIN = 0
    HERO = 1
