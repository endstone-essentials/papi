#include <endstone_papi/papi.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// NOTE: we need this wrapper to EXPLICITLY get the reference to papi::PlaceholderAPI.
// Down casting a C++ type cannot be easily done in Python but is easy to do in C++ with static_cast.
// Let's keep it like this until I find a cleaner way one day.
class PyPlaceholderAPI {
public:
    explicit PyPlaceholderAPI(endstone::Plugin &plugin)
    {
        if (plugin.getServer().getPluginManager().isPluginEnabled("papi")) {
            plugin_ = static_cast<papi::PlaceholderAPI *>(plugin.getServer().getPluginManager().getPlugin("papi"));
        }
    }

    std::string setPlaceholder(const endstone::Player &player, std::string_view text)
    {
        if (!plugin_) {
            throw std::runtime_error("PlaceholderAPI is not enabled!");
        }
        return plugin_->setPlaceholder(player, text);
    }
    // TODO(daoge): don't forget to add a wrapper function here whenever you add a method in PlaceholderAPI

private:
    papi::PlaceholderAPI *plugin_ = nullptr;
};

PYBIND11_MODULE(_papi, m)
{
    py::object plugin = py::module_::import("endstone.plugin").attr("Plugin");

    py::class_<PyPlaceholderAPI>(m, "PlaceholderAPI")
        .def(py::init<endstone::Plugin &>(), py::arg("plugin"))
        .def("set_placeholder", &PyPlaceholderAPI::setPlaceholder, py::arg("player"), py::arg("text"),
             "Translates all placeholders into their corresponding values.");
    // TODO(daoge): add more bindings here if needed
}
