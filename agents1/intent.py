from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Intent:
    """Represents an intent of an agent to do something."""

    # The type of the intent
    what: str

    # The area that the intent is about
    area: int | None = None