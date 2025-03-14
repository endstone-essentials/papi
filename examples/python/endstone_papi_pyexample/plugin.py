from endstone_papi import PlaceholderAPI
from endstone.plugin import Plugin
from endstone.event import event_handler, EventPriority, PlayerJoinEvent


class JoinExample(Plugin):
    api_version = "0.6"
    soft_depend = ["papi"]

    def __init__(self):
        super().__init__()
        self.papi: PlaceholderAPI | None = None

    def on_enable(self):
        if self.server.plugin_manager.is_plugin_enabled("papi"):
            self.register_events(self)
            self.papi = self.server.service_manager.load("PlaceholderAPI")
        else:
            self.logger.warning("Could not find PlaceholderAPI! This plugin is required.")
            self.server.plugin_manager.disable_plugin(self)

    @event_handler(priority=EventPriority.HIGHEST)
    def on_player_join(self, event: PlayerJoinEvent):
        join_text = "{player_name} joined the server! Their game mode is {player_gamemode}"
        join_text = self.papi.set_placeholder(event.player, join_text)
        event.join_message = join_text
