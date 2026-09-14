"""No pygame import anywhere in this file — that's the point.
If this file can only pass with pygame installed and a display available,
the core/backend separation has been broken somewhere.
"""
from pygext.core import GameObject, Scene, Vector2


class Mover(GameObject):
    def __init__(self, x: float, y: float, vx: float, vy: float) -> None:
        super().__init__(x, y)
        self.velocity = Vector2(vx, vy)

    def update(self, dt: float) -> None:
        self.position = self.position + self.velocity * dt


def test_scene_updates_objects():
    scene = Scene()
    mover = scene.add(Mover(0, 0, 10, 0))

    scene.update(dt=1.0)

    assert mover.position == Vector2(10, 0)


def test_scene_sweeps_dead_objects():
    scene = Scene()
    obj = scene.add(GameObject())
    obj.kill()

    scene.update(dt=1.0)

    assert obj not in scene.objects


def test_objects_of_type_filters_correctly():
    scene = Scene()
    scene.add(Mover(0, 0, 0, 0))
    scene.add(GameObject())

    movers = scene.objects_of_type(Mover)

    assert len(movers) == 1
