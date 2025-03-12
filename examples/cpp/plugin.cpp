#include <endstone/endstone.hpp>
#include <endstone_papi/papi.h>

class JoinExample : public endstone::Plugin {
public:
    void onEnable() override
    {
        if (getServer().getPluginManager().isPluginEnabled("papi")) {
            registerEvent(&JoinExample::onPlayerJoin, *this, endstone::EventPriority::Highest);
        }
        else {
            getLogger().warning("Could not find PlaceholderAPI! This plugin is required.");
            getServer().getPluginManager().disablePlugin(*this);
        }
    }

    void onPlayerJoin(endstone::PlayerJoinEvent &event)
    {
        std::string join_text = "{player_name} joined the server! Their game mode is {player_gamemode}";
        auto &papi = *static_cast<papi::PlaceholderAPI *>(getServer().getPluginManager().getPlugin("papi"));
        join_text = papi.setPlaceholder(event.getPlayer(), join_text);
        event.setJoinMessage(join_text);
    }
};

ENDSTONE_PLUGIN(/*name=*/"papi_example", /*version=*/"0.0.1", /*main_class=*/JoinExample)
{
    prefix = "PlaceholderAPI Example";
    description = "An example plugin that depends on the Placeholder API";
    website = "https://github.com/endstone-essentials/papi";
    authors = {"Vincent <magicdroidx@gmail.com>"};
    soft_depend = {"papi"};
}
