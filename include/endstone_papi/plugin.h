#pragma once

#include "endstone_papi/papi.h"

#include <endstone/endstone.hpp>

namespace papi {
class PlaceholderAPIPlugin : public endstone::Plugin, public PlaceholderAPI {
public:
};
} // namespace papi
