import re
import datetime

from typing import Callable
from endstone.plugin import Plugin
from ._papi import PlaceholderAPI as IPlaceholderAPI
from endstone import Player
from .chars_replacer import apply


class PlaceholderAPI(IPlaceholderAPI):
    def __init__(self, plugin: Plugin):
        IPlaceholderAPI.__init__(self)
        self._plugin = plugin
        self._registry: dict[str, Callable[[Player, str], str]] = {}
        self._placeholder_pattern = re.compile(r"[{]([^{}]+)[}]")
        self._register_default_placeholders()

    def set_placeholders(self, player: Player, text: str) -> str:
        """
        Translates all placeholders into their corresponding values.
        The pattern of a valid placeholder is {<identifier>:<params>}.

        Args:
            player (Player): Player to parse the placeholders against.
            text (str): Text to set the placeholder values in.

        Returns:
            str: String containing all translated placeholders.
        """
        return apply(player, text, self._registry)

    def is_registered(self, identifier: str) -> bool:
        return identifier in self._registry

    @property
    def registered_identifiers(self):
        return self._get_registered_identifiers()

    def _get_registered_identifiers(self) -> list[str]:
        return list(self._registry.keys())

    @property
    def placeholder_pattern(self):
        return self._get_placeholder_pattern()

    def _get_placeholder_pattern(self) -> str:
        return self._placeholder_pattern.pattern

    def contains_placeholders(self, text: str) -> bool:
        return self._placeholder_pattern.search(text) is not None

    def register_placeholder(
            self,
            plugin: Plugin,
            identifier: str,
            processor: Callable[[Player, str], str],
    ) -> bool:
        # TODO(daoge): duplicate placeholders are not allowed in the current design, shall we implement namespaces?
        if self.is_registered(identifier):
            identifier = f"{plugin.name}:{identifier}"
        if self.is_registered(identifier):
            self._plugin.logger.warning(
                f"Plugin {plugin.name} trying to register a duplicate placeholder: {identifier}"
            )
            return False

        self._registry[identifier] = processor
        return True

    def _register_default_placeholders(self):
        self.register_placeholder(
            self._plugin, "x", lambda player, params: str(int(player.location.x))
        )
        self.register_placeholder(
            self._plugin, "y", lambda player, params: str(int(player.location.y))
        )
        self.register_placeholder(
            self._plugin, "z", lambda player, params: str(int(player.location.z))
        )
        self.register_placeholder(
            self._plugin, "player_name", lambda player, params: player.name
        )
        self.register_placeholder(
            self._plugin,
            "dimension",
            lambda player, params: player.location.dimension.type.name.lower(),
        )
        self.register_placeholder(
            self._plugin,
            "dimension_id",
            lambda player, params: player.location.dimension.type.value,
        )
        self.register_placeholder(
            self._plugin, "ping", lambda player, params: player.ping
        )
        self.register_placeholder(
            self._plugin,
            "mc_version",
            lambda player, params: self._plugin.server.minecraft_version,
        )
        self.register_placeholder(
            self._plugin,
            "online",
            lambda player, params: str(len(self._plugin.server.online_players)),
        )
        self.register_placeholder(
            self._plugin,
            "max_online",
            lambda player, params: str(self._plugin.server.max_players),
        )
        self.register_placeholder(
            self._plugin,
            "date",
            lambda player, params: datetime.datetime.today().strftime("%x"),
        )
        self.register_placeholder(
            self._plugin,
            "time",
            lambda player, params: datetime.datetime.today().strftime("%X"),
        )
        self.register_placeholder(
            self._plugin,
            "datetime",
            lambda player, params: datetime.datetime.today().strftime("%c"),
        )
        self.register_placeholder(
            self._plugin,
            "year",
            lambda player, params: datetime.datetime.today().strftime("%Y"),
        )
        self.register_placeholder(
            self._plugin,
            "month",
            lambda player, params: datetime.datetime.today().strftime("%m"),
        )
        self.register_placeholder(
            self._plugin,
            "day",
            lambda player, params: datetime.datetime.today().strftime("%d"),
        )
        self.register_placeholder(
            self._plugin,
            "hour",
            lambda player, params: datetime.datetime.today().strftime("%H"),
        )
        self.register_placeholder(
            self._plugin,
            "minute",
            lambda player, params: datetime.datetime.today().strftime("%M"),
        )
        self.register_placeholder(
            self._plugin,
            "second",
            lambda player, params: datetime.datetime.today().strftime("%S"),
        )
        self.register_placeholder(
            self._plugin, "address", lambda player, params: player.address
        )
        self.register_placeholder(
            self._plugin, "runtime_id", lambda player, params: player.runtime_id
        )
        self.register_placeholder(
            self._plugin, "exp_level", lambda player, params: player.exp_level
        )
        self.register_placeholder(
            self._plugin, "total_exp", lambda player, params: player.total_exp
        )
        self.register_placeholder(
            self._plugin, "exp_progress", lambda player, params: player.exp_progress
        )
        self.register_placeholder(
            self._plugin,
            "game_mode",
            lambda player, params: player.game_mode.name.lower(),
        )
        self.register_placeholder(
            self._plugin, "xuid", lambda player, params: player.xuid
        )
        self.register_placeholder(
            self._plugin, "uuid", lambda player, params: player.unique_id
        )
        self.register_placeholder(
            self._plugin, "device_os", lambda player, params: player.device_os
        )
        self.register_placeholder(
            self._plugin, "locale", lambda player, params: player.locale
        )
