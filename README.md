#Alpha Code

from typing import Optional
from game.logic.base import
from game.models import GameObject, Board, Position

class SuperBot(BaseLogic):
    def _init_(self):
        super()._init_()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None 
        self.current_direction = 0 
        self.my_attribute = 0 

    def clamp(self, n, smallest, largest) -> int:
        return max(smallest, min(n, largest))

    def position_equals(self, a: Position, b: Position) -> bool:
        return a.x == b.x and a.y == b.y

    def get_direction_Adv(self, current_x: int, current_y: int, dest_x: int, dest_y: int, avoidList) -> tuple[int, int]:
        list_posisi_dihindari = [(pos.x, pos.y) for pos in avoidList]

        delta_x = self.clamp(dest_x - current_x, -1, 1)
        delta_y = self.clamp(dest_y - current_y, -1, 1)

        if delta_x == 0 and delta_y == 0:
            return 0, 0

        if delta_x != 0:
            next_x_tentative = current_x + delta_x
            if (next_x_tentative, current_y) not in list_posisi_dihindari:
                return delta_x, 0 
                
        if delta_y != 0:
            next_y_tentative = current_y + delta_y
            if (current_x, next_y_tentative) not in list_posisi_dihindari:
                return 0, delta_y
                
        if delta_x != 0 and delta_y != 0:
            # Coba bergerak diagonal
            if (current_x + delta_x, current_y + delta_y) not in list_posisi_dihindari:
                return delta_x, delta_y

        for dx, dy in possible_moves:
            next_x, next_y = current_x + dx, current_y + dy
            if (next_x, next_y) not in list_posisi_dihindari:
                return dx, dy
        return 0, 0
