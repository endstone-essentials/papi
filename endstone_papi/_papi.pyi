from endstone.plugin import Service
from endstone import Player

__all__ = ['PlaceholderAPI']


class PlaceholderAPI(Service):
    def set_placeholder(self, player: Player, text: str) -> str:
        """
        Translates all placeholders into their corresponding values.
        The pattern of a valid placeholder is {<identifier>:<params>}.

        Args:
            player (Player): Player to parse the placeholders against.
            text (str): Text to set the placeholder values in.

        Returns:
            str: String containing all translated placeholders.
        """
