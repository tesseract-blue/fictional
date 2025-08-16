from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Node(BaseModel):
    model_config = ConfigDict(
        use_attribute_docstrings=True,
        arbitrary_types_allowed=True,
    )


class Place(Node):
    # spatiotemporal region?
    ...


class Event(Node): ...


class Locale(Node):
    name: ...

    @property
    def sub_locales(self) -> list[Locale]:
        """
        The locales contained within this locale.
        For instance if this locale is a tavern,
        one sub locale might be the bar area.
        """
        ...

    @property
    def super_locale(self) -> Locale:
        """
        The locale that spatially contains this locale.
        For instance if this locale is a bar, then the
        super locale could be a tavern.
        """
        ...

    @property
    def adjacent_locales(self) -> list[Locale]:
        """ """
        ...


class Realm(Locale):
    """
    This is the 'master' locale containing all other
    locales throughout the world. The parents of any
    given locale will always terminate here.
    """

    ...


class GlobalContext(BaseModel):
    world: str = Field(examples=["Wild West"])
    period: ...


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

    name: str = Field(examples=["John Doe"])
    role: str | None = Field(
        default=None,
        examples=["salesman"],
    )
    traits: list[str] = Field(
        default_factory=list,
        examples=[""],
    )
    beliefs: list[str] = Field(default_factory=list)

    def initialize(self) -> None:
        """
        This should initialize the agent in a specific local context for the player
        to interact with.

        It should have:
        - time of day
        - previous conversations
        - current locale
        """
        ...
