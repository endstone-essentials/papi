#pragma once

#include <endstone/endstone.hpp>

namespace papi {
class PlaceholderAPI : public endstone::Service {
public:
    /**
     * Translates all placeholders into their corresponding values.
     * <br>The pattern of a valid placeholder is <code>{<identifier>:<params>}</code>.
     *
     * @param player Player to parse the placeholders against
     * @param text Text to set the placeholder values in
     * @return String containing all translated placeholders
     */
    [[nodiscard]] virtual std::string setPlaceholder(const endstone::Player &player, std::string_view text) const = 0;

    // TODO(daoge): we define the interface here so both C++ and Python knows how to interop with each other
    //  https://github.com/PlaceholderAPI/PlaceholderAPI/blob/master/src/main/java/me/clip/placeholderapi/PlaceholderAPI.java
    //  we need methods e.g.:
    //  - isRegistered
    //  - getRegisteredIdentifiers
    //  - getPlaceholderPattern (let's use bracket instead of percentage)
    //  - containsPlaceholders
    //  - registerExpansion
};
} // namespace papi
