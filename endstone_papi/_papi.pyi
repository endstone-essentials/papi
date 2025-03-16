from __future__ import annotations

from typing import Callable

from endstone import Player
from endstone.plugin import Service, Plugin

__all__ = ["PlaceholderAPI"]


class PlaceholderAPI(Service):
    def __init__(self) -> None: ...

    def _get_placeholder_pattern(self) -> str:
        """
        Get the normal placeholder pattern.
        """

    def _get_registered_identifiers(self) -> list[str]:
        """
        Get all registered placeholder identifiers.
        """

    def contains_placeholders(self, text: str) -> bool:
        """
        Check if a String contains any placeholders.
        """

    def is_registered(self, identifier: str) -> bool:
        """
        Check if a specific placeholder identifier is currently registered.
        """

    def register_placeholder(
            self,
            plugin: Plugin,
            identifier: str,
            processor: Callable[[Player | None, str], str],
    ) -> bool:
        """
        Attempt to register a placeholder.
        """

    def set_placeholders(self, player: Player | None, text: str) -> str:
        """
        Translates all placeholders into their corresponding values.
        """
