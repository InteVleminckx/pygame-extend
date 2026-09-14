"""The one place allowed to know both pygame's key constants and our
generic Action enum. Everything downstream only sees InputEvent.
"""
from __future__ import annotations

import pygame

from pygext.core.events import Action, InputEvent, InputState

_KEY_TO_ACTION = {
    pygame.K_UP: Action.UP,
    pygame.K_w: Action.UP,
    pygame.K_DOWN: Action.DOWN,
    pygame.K_s: Action.DOWN,
    pygame.K_LEFT: Action.LEFT,
    pygame.K_a: Action.LEFT,
    pygame.K_RIGHT: Action.RIGHT,
    pygame.K_d: Action.RIGHT,
    pygame.K_RETURN: Action.CONFIRM,
    pygame.K_SPACE: Action.CONFIRM,
    pygame.K_ESCAPE: Action.CANCEL,
    pygame.K_p: Action.PAUSE,
}


def translate(event: "pygame.event.Event") -> InputEvent | None:
    """Return a generic InputEvent for a pygame event, or None if it's
    not an input event we care about (mouse motion, window focus, ...).
    """
    if event.type == pygame.QUIT:
        return InputEvent(Action.QUIT, InputState.PRESSED)

    if event.type == pygame.KEYDOWN and event.key in _KEY_TO_ACTION:
        return InputEvent(_KEY_TO_ACTION[event.key], InputState.PRESSED)

    if event.type == pygame.KEYUP and event.key in _KEY_TO_ACTION:
        return InputEvent(_KEY_TO_ACTION[event.key], InputState.RELEASED)

    return None
