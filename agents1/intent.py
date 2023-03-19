from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Intent:
    """Represents an intent of an agent to do something."""

    # The type of the intent
    what: str

    # The time at which the intent was created
    time: int | None = None

    # The time at which the intent was fulfilled
    fulfilledTime: int | None = None

    # The target of the intent (area or victim)
    target: int | None = None