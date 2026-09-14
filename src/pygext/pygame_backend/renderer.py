"""Draws a Scene without the Scene's objects needing to know they're
being drawn.

Usage:
    renderer = Renderer()
    renderer.register(PacMan, draw_pacman)
    renderer.register(Ghost, draw_ghost)
    ...
    renderer.draw_scene(scene, window.surface)

`draw_fn` signature: (obj: GameObject, surface: pygame.Surface) -> None
"""
from __future__ import annotations

from typing import Callable

import pygame

from pygext.core.game_object import GameObject
from pygext.core.scene import Scene

DrawFn = Callable[[GameObject, "pygame.Surface"], None]


class Renderer:
    def __init__(self) -> None:
        self._draw_fns: dict[type, DrawFn] = {}

    def register(self, obj_type: type, draw_fn: DrawFn) -> None:
        self._draw_fns[obj_type] = draw_fn

    def draw_scene(self, scene: Scene, surface: "pygame.Surface") -> None:
        for obj in scene.objects:
            draw_fn = self._draw_fns.get(type(obj))
            if draw_fn is not None:
                draw_fn(obj, surface)
