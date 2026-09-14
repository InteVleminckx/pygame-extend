# pygame-extend (pygext)

A small toolkit for pygame projects that keeps game **logic** separate from
**rendering**, so your game state is testable and runnable with no display.

## Layout

```
pygext.core            # zero pygame imports
    Vector2             # minimal 2D vector
    GameObject           # base class for anything with state/behavior
    Scene                 # owns + updates a list of GameObjects
    Action, InputEvent      # generic input, not pygame key constants

pygext.pygame_backend  # depends on pygame and on pygext.core
    Window               # sets up the display
    BaseGame              # dt/fps loop; inherit and implement 3 methods
    Renderer               # maps GameObject type -> draw function
    translate                # pygame.event.Event -> InputEvent
```

## Usage

```python
from pygext.core import GameObject, Scene, Vector2, Action, InputState
from pygext.pygame_backend import BaseGame, Window, Renderer
import pygame


class Player(GameObject):
    def __init__(self):
        super().__init__(x=100, y=100)
        self.speed = 200  # px/sec

    def update(self, dt):
        # pure logic, no pygame here
        pass


def draw_player(obj, surface):
    pygame.draw.circle(surface, (255, 255, 0), obj.position.as_tuple(), 12)


class MyGame(BaseGame):
    def setup(self):
        self.scene = Scene()
        self.player = self.scene.add(Player())
        self.renderer = Renderer()
        self.renderer.register(Player, draw_player)

    def update(self, dt):
        self.scene.update(dt)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.renderer.draw_scene(self.scene, surface)

    def handle_input(self, event):
        if event.action == Action.LEFT and event.state == InputState.PRESSED:
            self.player.position.x -= 10


if __name__ == "__main__":
    window = Window(800, 600, title="My Game")
    MyGame(window).run()
```

## Testing game logic without a display

Because `pygext.core` never imports pygame, you can unit test your game
objects directly:

```python
from pygext.core import Scene
from mygame.entities import Player

def test_player_moves():
    scene = Scene()
    player = scene.add(Player())
    scene.update(dt=1.0)
    assert player.position.x > 0
```

No `pygame.init()`, no display, no `SDL_VIDEODRIVER=dummy` workarounds.

## Installing as a dependency (Poetry)

From a git repo, in another project's `pyproject.toml`:

```toml
[tool.poetry.dependencies]
pygame-extend = { git = "https://github.com/InteVleminckx/pygame-extend.git", extras = ["pygame"] }
```

Or for local development against a checked-out copy:

```toml
[tool.poetry.dependencies]
pygame-extend = { path = "../pygame-extend", develop = true, extras = ["pygame"] }
```

Then `poetry install` as usual. The `pygame` extra is optional — omit it if
a project only needs `pygext.core` and never touches the pygame backend
(e.g. a headless simulation or an AI training loop).

Uses [pygame-ce](https://pyga.me/) (the community fork) rather than the
original `pygame` package — same `import pygame`, actively maintained.
Don't install both in the same environment; they conflict.

## Design rule

If a file under `pygext/core/` ever needs `import pygame`, that's a sign
something rendering-related leaked into logic — move it to
`pygame_backend` instead.
