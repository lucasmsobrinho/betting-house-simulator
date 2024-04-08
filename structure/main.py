from dataclasses import dataclass
from typing import List

PROFILES = {
    "random": {
        "risk": (lambda x, y: x + y),
        "nope": (lambda a, b, c: a * b * c)
    }
}

class House:
    def __init__(self, N: int):
        self.N = N # number of games


class Player:
    money: float
    profile: string
    bets: List[Bet]

    def __init__(self, id, money, profile):
        self.money = money
        self.profile = profile
        self.bets = []

    def risk(self) -> bool:
        '''decide if the player will bet in the game or not'''
        pass

    def position(self) -> int:
        '''decide which team the player will bet on'''
        pass

    def allocation(self) -> float:
        '''decide how much money the player will bet'''
        pass


class Game:
    bet_list: List[Bet]
    mult_a: float
    mult_b: float

    def __init__(self, N: int,
            prob: float,
            max_t: int,
            house_estimate: float)
        self.N = N
        self.prob = prob
        self.max_t = max_t
        self.time = 0
        self.house_estimate = house_estimate


@dataclass
class Bet:
    game : Game
    player : Player
    value : float
    team : int
    multi : float







# Games: N x T x 2
# N: n games
# T: max time game
# 2: n of teams

# Players
# 
# 
# 
# 




