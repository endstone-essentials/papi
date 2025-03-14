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
        PYBIND11_OVERRIDE_PURE_NAME(std::string, PlaceholderAPI, "set_placeholder", setPlaceholder);
    }
};

PYBIND11_MODULE(_papi, m)
{
    py::class_<papi::PlaceholderAPI, PyPlaceholderAPI, std::shared_ptr<papi::PlaceholderAPI>>(m, "PlaceholderAPI")
        .def(py::init<>())
        .def("set_placeholder", &papi::PlaceholderAPI::setPlaceholder, py::arg("player"), py::arg("text"),
             "Translates all placeholders into their corresponding values.");
    // TODO(daoge): add more bindings here if needed
}
