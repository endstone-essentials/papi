cmake_minimum_required(VERSION 3.15)

project(papi CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
        endstone
        GIT_REPOSITORY https://github.com/EndstoneMC/endstone.git
        GIT_TAG v0.6.2
)
FetchContent_MakeAvailable(endstone)

if (NOT CMAKE_SOURCE_DIR STREQUAL PROJECT_SOURCE_DIR)
    add_library(endstone_papi INTERFACE)
    target_include_directories(endstone_papi INTERFACE include)
    target_link_libraries(endstone_papi INTERFACE endstone::endstone)
    return()
endif ()

if (NOT DEFINED SKBUILD)
    endstone_add_plugin(${PROJECT_NAME} src/plugin.cpp)
    target_include_directories(${PROJECT_NAME} PRIVATE include)

    option(PAPI_BUILD_EXAMPLE "Build the PlaceholderAPI example plugin" OFF)
    if (NOT PAPI_BUILD_EXAMPLE STREQUAL OFF)
        add_subdirectory(examples/cpp)
    endif ()
else ()
    execute_process(
            COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
            OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE pybind11_ROOT)
    find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
    find_package(pybind11 CONFIG REQUIRED)

    pybind11_add_module(_${PROJECT_NAME} endstone_papi/_papi.cpp)
    target_include_directories(_${PROJECT_NAME} PRIVATE include)
    target_link_libraries(_${PROJECT_NAME} PRIVATE endstone::endstone)
    install(TARGETS _papi DESTINATION "endstone_papi" COMPONENT python)
endif ()