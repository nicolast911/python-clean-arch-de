from dataclasses import dataclass
from typing import TYPE_CHECKING

from .base_classes import Action, GameObject
from .location import Location

if TYPE_CHECKING:
    from .player import Player


@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def execute(self, instigator: "Player") -> None:
        instigator.location = self.target


@dataclass
class SkipTurnAction(Action):
    @property
    def description(self) -> str:
        return "wait one turn"

    def execute(self, instigator: "Player") -> None:
        # Do nothing...
        pass


@dataclass
class InspectAction(Action):
    object: GameObject

    @property
    def description(self) -> str:
        return f"inspect {self.object}"

    def execute(self, instigator: "Player") -> None:
        pass
