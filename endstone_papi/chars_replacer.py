from typing import Callable

from endstone import Player

HEAD = "{"
TAIL = "}"


def apply(
        player: Player | None,
        text: str,
        lookup: dict[str, Callable[[Player, str], str]],
) -> str:
    builder = []
    i = 0
    length = len(text)

    while i < length:
        l = text[i]
        if l != HEAD or i + 1 >= length:
            builder.append(l)
            i += 1
            continue

        identified = False
        invalid = True
        had_space = False
        identifier_chars = []
        parameters_chars = []

        i += 1

        while i < length:
            p = text[i]
            if p == " " and not identified:
                had_space = True
                break
            if p == TAIL:
                invalid = False
                break
            if p == "|" and not identified:
                identified = True
                i += 1
                continue
            if identified:
                parameters_chars.append(p)
            else:
                identifier_chars.append(p)
            i += 1

        identifier_str = "".join(identifier_chars)
        parameters_str = "".join(parameters_chars)

        if invalid:
            builder.append(HEAD + identifier_str)
            if identified:
                builder.append(
                    "|" + parameters_str
                )
            if had_space:
                builder.append(" ")
            i += 1
            continue

        placeholder = lookup.get(identifier_str, None)
        if placeholder is None:
            builder.append(HEAD + identifier_str)
            if identified:
                builder.append("|")
            builder.append(parameters_str + TAIL)
            i += 1
            continue

        replacement = placeholder(player, parameters_str)
        if replacement is None:
            builder.append(HEAD + identifier_str)
            if identified:
                builder.append("|")
            builder.append(parameters_str + TAIL)
            i += 1
            continue

        builder.append(replacement)
        i += 1

    return "".join(builder)
