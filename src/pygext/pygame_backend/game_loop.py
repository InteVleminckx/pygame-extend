from __future__ import annotations

from abc import ABC, abstractmethod

import pygame

from pygext.core.events import Action, InputEvent, InputState

from .input_adapter import translate
from .window import Window


class BaseGame(ABC):
    """Inherit from this and implement update / draw / handle_input.

    The loop itself (dt tracking, fps cap, event pump) lives here so
    subclasses only ever write game-specific code.
    """

    def __init__(self, window: Window) -> None:
        self.window = window
        self.clock = pygame.time.Clock()
        self.running = True

    def setup(self) -> None:
        """Optional one-time setup, called once before the loop starts."""

    @abstractmethod
    def update(self, dt: float) -> None:
        """Advance game state by dt seconds (seconds, not ms)."""

    @abstractmethod
    def draw(self, surface: "pygame.Surface") -> None:
        """Draw the current state to the given surface."""

    @abstractmethod
    def handle_input(self, event: InputEvent) -> None:
        """React to one generic input event."""

    def run(self) -> None:
        self.setup()
        while self.running:
            dt = self.clock.tick(self.window.fps) / 1000.0

            for raw_event in pygame.event.get():
                input_event = translate(raw_event)
                if input_event is None:
                    continue
                if (
                    input_event.action is Action.QUIT
                    and input_event.state is InputState.PRESSED
                ):
                    self.running = False
                self.handle_input(input_event)

            self.update(dt)
            self.draw(self.window.surface)
            pygame.display.flip()

        self.window.close()
