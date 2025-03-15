#include <endstone_papi/papi.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Trampoline class, see:
// https://pybind11.readthedocs.io/en/stable/advanced/classes.html#overriding-virtual-functions-in-python
class PyPlaceholderAPI : public papi::PlaceholderAPI {
public:
    using PlaceholderAPI::PlaceholderAPI;

    [[nodiscard]] std::string setPlaceholder(const endstone::Player &player, std::string_view text) const override
    {
        PYBIND11_OVERRIDE_PURE_NAME(std::string, PlaceholderAPI, "set_placeholder", setPlaceholder, player, text);
    }

    [[nodiscard]] std::vector<std::string> setPlaceholder(const endstone::Player &player, std::vector<std::string_view> texts) const override
    {
        PYBIND11_OVERRIDE_PURE_NAME(std::vector<std::string>, PlaceholderAPI, "set_placeholder", setPlaceholder, player, texts);
    }

    [[nodiscard]] bool isRegistered(std::string_view identifier) const override
    {
        PYBIND11_OVERRIDE_PURE_NAME(bool, PlaceholderAPI, "is_registered", isRegistered, identifier);
    }

    [[nodiscard]] std::vector<std::string> getRegisteredIdentifiers() const override
    {
        PYBIND11_OVERRIDE_PURE_NAME(std::vector<std::string>, PlaceholderAPI, "get_registered_identifiers", getRegisteredIdentifiers);
    }

    // TODO: getPlaceholderPattern

    [[nodiscard]] bool containsPlaceholders(std::string_view text) const override
    {
        PYBIND11_OVERRIDE_PURE_NAME(bool, PlaceholderAPI, "contains_placeholders", containsPlaceholders, text);
    }

    [[nodiscard]] bool registerPlaceholder(endstone::Plugin &plugin, std::string_view identifier, std::function<std::string(std::optional<endstone::Player&>, std::optional<std::string>)> processor) const override
    {
        PYBIND11_OVERRIDE_PURE_NAME(bool, PlaceholderAPI, "register_placeholder", registerPlaceholder, plugin, identifier, processor);
    }
};

PYBIND11_MODULE(_papi, m)
{
    py::module_::import("endstone");
    py::module_::import("endstone.plugin");

    py::class_<papi::PlaceholderAPI, PyPlaceholderAPI, endstone::Service, std::shared_ptr<papi::PlaceholderAPI>>(
        m, "PlaceholderAPI")
        .def(py::init<>())
        .def("set_placeholder", &papi::PlaceholderAPI::setPlaceholder, py::arg("player"), py::arg("text"),
             "Translates all placeholders into their corresponding values.")
        .def("set_placeholder", &papi::PlaceholderAPI::setPlaceholder, py::arg("player"), py::arg("texts"),
             "Translates all placeholders into their corresponding values.")
        .def("is_registered", &papi::PlaceholderAPI::isRegistered, py::arg("identifier"),
            "Check if a specific placeholder identifier is currently registered.")
        .def("get_registered_identifiers", &papi::PlaceholderAPI::getRegisteredIdentifiers,
            "Get all registered placeholder identifiers.")
        .def("contains_placeholders", &papi::PlaceholderAPI::containsPlaceholders, py::arg("text"),
            "Check if a String contains any placeholders.")
        .def("register_placeholder", &papi::PlaceholderAPI::registerPlaceholder, py::arg("plugin"), py::arg("identifier"), py::arg("processor"),
            "Attempt to register a placeholder.");
}
