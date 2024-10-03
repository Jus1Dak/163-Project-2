from Character import *
from coord import *


class Villian(Character, ABC):
    def __init__(self):
        super().__init__(player= 0)

