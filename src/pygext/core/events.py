"""Generic input representation.

If game logic ever needs to react to input, it should take these types,
never a raw pygame.event.Event or a pygame key constant. The pygame
backend is responsible for translating its events into these.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class Action(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    CONFIRM = auto()
    CANCEL = auto()
    PAUSE = auto()
    QUIT = auto()


class InputState(Enum):
    PRESSED = auto()
    RELEASED = auto()


@dataclass(frozen=True)
class InputEvent:
    action: Action
    state: InputState
