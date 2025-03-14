from ._papi import PlaceholderAPI as _PlaceholderAPI
from endstone import Player


class PlaceholderAPI(_PlaceholderAPI):
    def __init__(self):
        _PlaceholderAPI.__init__(self)

    def set_placeholder(self, player: Player, text: str) -> str:
        # TODO: implement this
        return text.format(player_name=player.name, player_gamemode=player.game_mode)
