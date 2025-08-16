from pydantic import BaseModel, ConfigDict, Field


class Node(BaseModel):
    model_config = ConfigDict(
        use_attribute_docstrings=True,
    )


class Place(Node):
    # spatiotemporal region?
    ...


class Event(Node): ...


class Agent(Node):
    name: str | None = None
    role: str | None = Field(
        default=None,
        examples=["merchant", "soldier"],
    )
    beliefs: list[str] = Field(default_factory=list)
