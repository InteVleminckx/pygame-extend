"""Base class for anything that has state and behavior in the game world.

A GameObject knows nothing about how (or whether) it's drawn. It is safe
to instantiate, update, and inspect in a test with no display, no pygame
import, and no event loop.
"""
from __future__ import annotations

from .vector import Vector2


class GameObject:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.position = Vector2(x, y)
        self.alive = True

    def update(self, dt: float) -> None:
        """Advance this object's state by dt seconds.

        Override in subclasses. Must not touch pygame, a surface, or
        anything rendering-related — only self.position and whatever
        other logic state the subclass defines.
        """

    def kill(self) -> None:
        """Mark for removal. Scene.update() sweeps dead objects each tick."""
        self.alive = False
