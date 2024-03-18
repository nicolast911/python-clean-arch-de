from abc import ABC, abstractmethod
from dataclasses import dataclass

from location_v2 import Location


class Action(ABC):
    @property
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def perform(self, instigator) -> None: ...


@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def perform(self, instigator) -> None:
        instigator.location = self.target


@dataclass
class SkipTurnAction(Action):
    @property
    def description(self) -> str:
        return "wait one turn"

    def perform(self, instigator) -> None:
        # Do nothing...
        pass
