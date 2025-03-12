# Placeholder API for Endstone

A Placeholder API plugin for Endstone, inspired by the famous PAPI plugin for Spigot. This project provides both native
C++ support and Python bindings via the `endstone_papi` package for seamless integration.

## Project Structure

```
endstone-essentials/papi/
├── endstone_papi/      # Python package for accessing the PAPI from Python
├── examples/
│   ├── cpp/            # C++ example plugin
│   └── python/         # Python example plugin
├── include/            # Header files
├── src/                # Implementation source code
├── CMakeLists.txt      # CMake build configuration
├── pyproject.toml      # Python package configuration
├── LICENSE             # License information
└── README.md           # This file
```

## Usages

### C++

```cpp
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
```

For the full codes, check our [C++ Example Plugin](examples/cpp).

### Python

```python
from endstone_papi import PlaceholderAPI
from endstone.plugin import Plugin
from endstone.event import event_handler, EventPriority, PlayerJoinEvent


class JoinExample(Plugin):
    api_version = "0.6"
    soft_depend = ["papi"]

    def on_enable(self):
        if self.server.plugin_manager.is_plugin_enabled("papi"):
            self.register_events(self)
            self.papi = PlaceholderAPI(self)
        else:
            self.logger.warning("Could not find PlaceholderAPI! This plugin is required.")
            self.server.plugin_manager.disable_plugin(self)

    @event_handler(priority=EventPriority.HIGHEST)
    def on_player_join(self, event: PlayerJoinEvent):
        join_text = "{player_name} joined the server! Their game mode is {player_gamemode}"
        join_text = self.papi.set_placeholder(event.player, join_text)
        event.join_message = join_text
```

For the full codes, check our [Python Example Plugin](examples/python).

## Contributing

Contributions are welcome! Feel free to fork the repository, improve the code, and submit pull requests with your
changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.