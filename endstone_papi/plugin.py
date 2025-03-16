from endstone import Player
from endstone.command import Command, CommandSender
from endstone.plugin import Plugin, ServicePriority

from .papi import PlaceholderAPI


class PlaceholderAPIPlugin(Plugin):
    api_version = "0.6"

    commands = {
        "papi": {
            "description": "PlaceholderAPI command",
            "usage": [
                "/papi parse <text: message> [player: player]",
                "/papi list",
            ],
            "permission": "papi.command.papi",
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
                text: str = args[1]
                player: Player | None = None
                if len(args) == 3:
                    player_name: str = args[2]
                    player = self.server.get_player(player_name)
                    if player is None:
                        sender.send_error_message(
                            f"Could not find player {player_name}!"
                        )
                        return False

                sender.send_message(self._api.set_placeholders(player, text))
            case "list":
                sender.send_message("Available placeholders:")
                for identifier in self._api.registered_identifiers:
                    sender.send_message(f"- {identifier}")

        return True
