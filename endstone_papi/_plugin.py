from endstone.plugin import Plugin, ServicePriority

from ._service import PlaceholderAPI


class PlaceholderAPIPlugin(Plugin):
    api_version = "0.6"

    def __init__(self):
        super().__init__()
        self._api = PlaceholderAPI()

    def on_load(self):
        self.server.service_manager.register("PlaceholderAPI", self._api, self, ServicePriority.HIGHEST)

    def on_disable(self):
        self.server.service_manager.unregister_all(self)
