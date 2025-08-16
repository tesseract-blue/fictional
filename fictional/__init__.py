from pydantic import BaseModel, Field


class Node(BaseModel): ...


class Place(Node):
    # spatiotemporal region?
    ...


class Event(Node): ...


class Agent(Node):
    name: str | None = None
    role: str | None = None
    beliefs: list[str] = Field(default_factory=list)
