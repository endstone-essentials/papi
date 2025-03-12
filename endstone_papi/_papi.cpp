#include <endstone_papi/papi.h>
#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

namespace nb = nanobind;

NB_MODULE(_papi, m)
{
    nb::class_<papi::PlaceholderAPI>(m, "PlaceholderAPI")
        .def("set_placeholder", &papi::PlaceholderAPI::setPlaceholder, nb::arg("player"), nb::arg("text"),
             "Translates all placeholders into their corresponding values.");
}
