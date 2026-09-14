from __future__ import annotations

import pygame


class Window:
    def __init__(
        self,
        width: int,
        height: int,
        title: str = "Game",
        fps: int = 60,
        flags: int = 0,
    ) -> None:
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.surface = pygame.display.set_mode((width, height), flags)
        pygame.display.set_caption(title)

    def close(self) -> None:
        pygame.quit()
