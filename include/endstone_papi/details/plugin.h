#pragma once

#include "endstone_papi/papi.h"

#include <endstone/endstone.hpp>

namespace papi::details {
class PlaceholderAPIPlugin : public PlaceholderAPI {
public:
    void onLoad() override;
    [[nodiscard]] std::string setPlaceholder(const endstone::Player &player, std::string_view text) const override;
};
} // namespace papi::details
