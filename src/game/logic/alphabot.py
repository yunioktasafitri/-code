from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from game.util import get_direction

class AlphaBot(BaseLogic):
    def __init__(self):
        super().__init__()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None

    def clamp(self, n, smallest, largest) -> int:
        return max(smallest, min(n, largest))

    def position_equals(self, a: Position, b: Position) -> bool:
        return a.x == b.x and a.y == b.y

    def get_direction_Adv(self, current_x, current_y, dest_x, dest_y, avoidList):
        avoid_set = {(pos.position.x, pos.position.y) for pos in avoidList}
        dx = self.clamp(dest_x - current_x, -1, 1)
        dy = self.clamp(dest_y - current_y, -1, 1)

        if dx == 0 and dy == 0:
            return 0, 0

        if dx != 0 and (current_x + dx, current_y) not in avoid_set:
            return dx, 0
        if dy != 0 and (current_x, current_y + dy) not in avoid_set:
            return 0, dy
        if dx != 0 and dy != 0 and (current_x + dx, current_y + dy) not in avoid_set:
            return dx, dy

        for alt_dx, alt_dy in self.directions:
            if (current_x + alt_dx, current_y + alt_dy) not in avoid_set:
                return alt_dx, alt_dy

        return 0, 0

    def next_move(self, board_bot: GameObject, board: Board) -> tuple[int, int]:
        props = board_bot.properties
        current_position = board_bot.position

        red_buttons = [obj for obj in board.game_objects if obj.type == "DiamondButtonGameObject"]
        teleporters = [obj for obj in board.game_objects if obj.type == "TeleportGameObject"]
        all_bots = board.bots
        diamonds = board.diamonds
        enemies = [b for b in all_bots if not self.position_equals(b.position, current_position)]

        # Prioritaskan red button jika ada yang jaraknya <= 5 blok
        nearest_btn = None
        min_btn_dist = float('inf')
        for btn in red_buttons:
            dist_btn = abs(current_position.x - btn.position.x) + abs(current_position.y - btn.position.y)
            if dist_btn <= 5 and dist_btn < min_btn_dist:
                nearest_btn = btn
                min_btn_dist = dist_btn
        if nearest_btn:
            return get_direction(current_position.x, current_position.y, nearest_btn.position.x, nearest_btn.position.y)

        # Setiap 15 detik cari dan tekan red button
        time_left = props.milliseconds_left // 1000
        if red_buttons and (time_left % 15 == 0):
            btn = red_buttons[0].position
            return get_direction(current_position.x, current_position.y, btn.x, btn.y)

        candidate_diamonds = []
        for d in diamonds:
            dist_us = abs(d.position.x - current_position.x) + abs(d.position.y - current_position.y)
            dist_enemy = min(
                (abs(e.position.x - d.position.x) + abs(e.position.y - d.position.y) for e in enemies),
                default=float('inf')
            )
            if dist_us < dist_enemy:
                points = d.properties.points
                dist_tp = float('inf')
                if len(teleporters) >= 2:
                    t1, t2 = teleporters[0], teleporters[1]
                    dist_tp = abs(current_position.x - t1.position.x) + abs(current_position.y - t1.position.y) + \
                              abs(t2.position.x - d.position.x) + abs(t2.position.y - d.position.y)
                best_dist = min(dist_us, dist_tp)
                density = (1.5 * points) / best_dist if best_dist > 0 else float('inf')
                candidate_diamonds.append((d, best_dist, points, density))

        steps_to_base = abs(current_position.x - props.base.x) + abs(current_position.y - props.base.y)
        if props.diamonds >= props.inventory_size or (steps_to_base + 2 >= time_left and props.diamonds > 0):
            return self.get_direction_Adv(current_position.x, current_position.y,
                                          props.base.x, props.base.y, [])

        if candidate_diamonds:
            candidate_diamonds.sort(key=lambda x: (-x[3], x[1]))
            target = candidate_diamonds[0][0].position
            return self.get_direction_Adv(current_position.x, current_position.y, target.x, target.y, teleporters)

        if red_buttons and props.diamonds < props.inventory_size:
            btn = red_buttons[0].position
            return get_direction(current_position.x, current_position.y, btn.x, btn.y)

        for dx, dy in self.directions:
            nx, ny = current_position.x + dx, current_position.y + dy
            if 0 <= nx < board.width and 0 <= ny < board.height:
                return dx, dy

        return 0, 0