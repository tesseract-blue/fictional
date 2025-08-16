from pydantic import BaseModel


class Node(BaseModel): ...


class Place(Node):
    # spatiotemporal region?
    ...


class Event(Node): ...


class Agent(Node): ...
