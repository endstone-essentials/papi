from endstone import Player
from endstone.command import Command, CommandSender
from endstone.plugin import Plugin, ServicePriority

from .papi import PlaceholderAPI


class PlaceholderAPIPlugin(Plugin):
    api_version = "0.6"

    commands = {
        "papi": {
            "description": "PlaceholderAPI command",
            "usages": [
                "/papi parse <player: player> <text: message>",
                "/papi list",
            ],
            "permissions": ["papi.command.papi"],
        }
    }

    permissions = {
        "papi.command.papi": {
            "description": "Allows users to use the /papi command",
            "default": "op",
        }
    }

    def __init__(self):
        super().__init__()
        self._api = PlaceholderAPI(self)

    def on_load(self):
        self.server.service_manager.register(
            "PlaceholderAPI", self._api, self, ServicePriority.HIGHEST
        )

    def on_disable(self):
        self.server.service_manager.unregister_all(self)

    def on_command(
            self, sender: CommandSender, command: Command, args: list[str]
    ) -> bool:
        match args[0]:
            case "parse":
                assert len(args) == 3, f"Invalid number of arguments! Expected 3, got {len(args)}."
                match args[1]:
                    case "me":
                        if not isinstance(sender, Player):
                            sender.send_error_message("You must be a player to use 'me' as a target!")
                            return True

                        player = sender

                    case "--null":
                        player = None

                    case player_name:
                        player = self.server.get_player(player_name)
                        if player is None:
                            sender.send_error_message(f"Could not find player {player_name}!")
                            return True

                text: str = args[2]
                sender.send_message(self._api.set_placeholders(player, text))

            case "list":
                sender.send_message("Available placeholders:")
                for identifier in self._api.registered_identifiers:
                    sender.send_message(f"- {identifier}")

        return True
