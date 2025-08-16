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
    """
    global:
    - setting/context (eg: fantasy world, sci fi space ship)

    constant:
    - name
    - role
    - personality traits / questions

    dynamic:
    - current setting/context (tavern, spacecraft docking bay)
    - entities in environment
    - available actions in reality (functions)
    - current objective or goal (eg: sell the player wares)
    """

    name: str | None = Field(
        default=None,
    )
    role: str | None = Field(
        default=None,
        examples=["merchant", "soldier"],
    )
    beliefs: list[str] = Field(default_factory=list)
