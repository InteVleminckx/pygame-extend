"""Owns the collection of GameObjects and steps them forward in time.

Scene is the thing you'd instantiate in a headless test or a training
loop for an AI — it never imports pygame.
"""
from __future__ import annotations

from .game_object import GameObject


class Scene:
    def __init__(self) -> None:
        self.objects: list[GameObject] = []

    def add(self, obj: GameObject) -> GameObject:
        self.objects.append(obj)
        return obj

    def remove(self, obj: GameObject) -> None:
        if obj in self.objects:
            self.objects.remove(obj)

    def update(self, dt: float) -> None:
        for obj in self.objects:
            obj.update(dt)
        # sweep anything that marked itself dead during this tick
        self.objects = [o for o in self.objects if o.alive]

    def objects_of_type(self, cls: type) -> list[GameObject]:
        return [o for o in self.objects if isinstance(o, cls)]
