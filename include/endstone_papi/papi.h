#pragma once

#include <endstone/endstone.hpp>

namespace papi {
class PlaceholderAPI {
public:
    virtual ~PlaceholderAPI() = default;

    /**
     * Translates all placeholders into their corresponding values.
     * <br>The pattern of a valid placeholder is <code>{<identifier>:<params>}</code>.
     *
     * @param player Player to parse the placeholders against
     * @param text Text to set the placeholder values in
     * @return String containing all translated placeholders
     */
    virtual std::string setPlaceholder(const endstone::Player &player, std::string_view text) = 0;
};
} // namespace papi
