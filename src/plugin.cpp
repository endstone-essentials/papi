#include "endstone_papi/details/plugin.h"

ENDSTONE_PLUGIN(/*name=*/"papi", /*version=*/"0.0.1", /*main_class=*/papi::details::PlaceholderAPIPlugin)
{
    prefix = "PlaceholderAPI";
    description = "A Placeholder Plugin for Endstone";
    website = "https://github.com/endstone-essentials/papi";
    authors = {"Vincent <magicdroidx@gmail.com>"};
}

namespace papi::details {
void PlaceholderAPIPlugin::onLoad()
{
    Plugin::onLoad();
}

std::string PlaceholderAPIPlugin::setPlaceholder(const endstone::Player &player, std::string_view text)
{
    // TODO: implement the actual functionality
    return std::string(text);
}

} // namespace papi::details
