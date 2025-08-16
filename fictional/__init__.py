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


class LocaleType(Node):
    """
    The locale type node is meant to define generic properties for classes of locales,
    which can be overridden by specific locales. The idea being that while every tavern
    is different, most taverns have stuff in common. We don't want all taverns to be copy
    and pasted versions of the same thing, but we don't want to have to duplicate attributes
    if it is a game with 100 taverns.
    """

    name: str = Field(examples=["tavern"])
    info: str = Field(examples=["A tavern for weary travelers."])
    # common_social_norms: str = Field(examples=["Fairly laid back"]) # TODO


class Locale(Node):
    """
    Other properties under consideration:

    - size
    - acoustic isolation / properties
    - capacity
    - typical occupants
    """

    name: str = Field(examples=["The Prancing Pony"])
    # specific_social_norms: str | None = None # TODO: This would probably encompass locale specific norms - like worship of a god in this tavern that isn't worshipped in other taverns.

    @property
    def type(self) -> LocaleType: ...

    @property
    def type_name(self) -> str:
        return self.type.name

    @property
    def type_info(self) -> str:
        return self.type.info

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

    @property
    def occupants(self) -> list[Agent]: ...


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
