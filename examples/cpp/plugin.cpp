#include <endstone/endstone.hpp>
#include <endstone_papi/papi.h>

class JoinExample : public endstone::Plugin {
public:
    void onEnable() override
    {
        if (getServer().getPluginManager().getPlugin("papi")) {
            registerEvent(&JoinExample::onPlayerJoin, *this, endstone::EventPriority::Highest);
            papi_ = getServer().getServiceManager().load<papi::PlaceholderAPI>("PlaceholderAPI");
        }
        else {
            getLogger().warning("Could not find PlaceholderAPI! This plugin is required.");
            getServer().getPluginManager().disablePlugin(*this);
        }
    }

    void onPlayerJoin(endstone::PlayerJoinEvent &event)
    {
        std::string join_text = "{player_name} joined the server! Their game mode is {player_gamemode}";
        join_text = papi_->setPlaceholders(&event.getPlayer(), join_text);
        event.setJoinMessage(join_text);
    }

private:
    std::shared_ptr<papi::PlaceholderAPI> papi_;
};

ENDSTONE_PLUGIN(/*name=*/"papi_example", /*version=*/"0.0.1", /*main_class=*/JoinExample)
{
    prefix = "PlaceholderAPI Example";
    description = "An example plugin that depends on the Placeholder API";
    website = "https://github.com/endstone-essentials/papi";
    authors = {"Vincent <magicdroidx@gmail.com>"};
    soft_depend = {"papi"};
}
