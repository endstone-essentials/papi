import re
import typing

from typing import Callable
from endstone.plugin import Plugin
from .pypapi import PlaceholderAPI as _PlaceholderAPI
from endstone import Player
from .chars_replacer import apply


class PlaceholderAPI(_PlaceholderAPI):
    def __init__(self, plugin: Plugin):
        _PlaceholderAPI.__init__(self)
        self._plugin = plugin
        self._registry = {}
        self._placeholder_pattern = re.compile(r"[{]([^{}]+)[}]")

    def set_placeholder(self, player: Player | None, text: str) -> str:
        return apply(player, text, self._registry.get)

    def is_registered(self, identifier: str) -> bool:
        return identifier in self._registry

    def get_registered_identifiers(self) -> list[str]:
        return list(self._registry.keys())

    def get_placeholder_pattern(self) -> re.Pattern[str]:
        return self._placeholder_pattern

    def contains_placeholders(self, text: str) -> bool:
        return self._placeholder_pattern.search(text) is not None

    def register_placeholder(self, plugin: Plugin, identifier: str,
                             processor: Callable[[Player | None, str | None], str]) -> bool:
        if self.is_registered(identifier):
            identifier = f"{plugin.name}:{identifier}"
        if self.is_registered(identifier):
            self._plugin.logger.warning(f"Plugin {plugin.name} trying to register a duplicate placeholder: {identifier}")
            return False

        self._registry[identifier] = processor
        return True
