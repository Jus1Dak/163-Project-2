from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from enum import Enum
from random import randint
from coord import Coord
from item import Potion


@abstractmethod
class Character:
    def __init__(self, player):
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
    def player(self, name):
        self.__player = name

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, num: int):
        self.__health = num

    @property
    def temp_health(self) -> int:
        return self.__temp_health

    @temp_health.setter
    def temp_health(self, num: int):
        self.__temp_health = num

    @property
    def combat(self) -> list:
        return self.combat

    @combat.setter
    def combat(self, lst: list):
        if not isinstance(self.__attack, int) and not isinstance(self.__defense, int):
            if self.__attack and self.__defense < 0:
                raise ValueError
            else:
                raise TypeError
        lst.extend([self.__attack, self.__defense])
        self.combat = lst


    @property
    def range(self) -> int:
        return self.__range

    @range.setter
    def range(self, num):
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
            if num < 1:
                raise ValueError
            else:
                raise TypeError
        self.__move = num

    def is_valid_check(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if 0 <= from_coord.x < len(board) and 0 <= from_coord.y < len(board[0]) and 0 <= to_coord.x < len(board) and 0 <= to_coord.y < len(board[0]): #checks to make sure indexs we are in the proper range
            if not from_coord.x == to_coord.x and not from_coord.y == to_coord.y:  # ensures that index from from_cord and to_cord aren't the same
                if board[from_coord.x][from_coord.y] == self.player and board[to_coord.x][to_coord.y] is None: #ensures player is in the starting cord and ending cord is empty
                    return True
        else:
            return False

    @abstractmethod
    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if self.is_valid_check:
            return True
        else:
            return False

    @abstractmethod
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if self.is_valid_check:
                return True
        else:
            return False

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
        damage = self.calculate_dice()
        target.temp_health -= damage
        print(f"{target} was dealt {damage} damage")


    @abstractmethod
    def __str__(self) -> str:
        return Character.__name__




class CharacterDeath(Exception):

    def __init__(self, msg, char: Character):
        self.message = msg


class InvalidAttack(Exception):
    pass


class Player(Enum):
    VILLAIN = 0
    HERO = 1