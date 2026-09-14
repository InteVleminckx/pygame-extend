"""A tiny, dependency-free 2D vector.

Deliberately NOT pygame.Vector2 — importing that here would pull pygame
into `core`, which is supposed to be usable (and testable) headlessly.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Vector2:
    x: float = 0.0
    y: float = 0.0

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def normalized(self) -> "Vector2":
        length = self.length()
        if length == 0:
            return Vector2(0.0, 0.0)
        return Vector2(self.x / length, self.y / length)

    def as_tuple(self) -> tuple[float, float]:
        return (self.x, self.y)
