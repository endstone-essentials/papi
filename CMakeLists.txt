cmake_minimum_required(VERSION 3.15)

project(papi CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
        endstone
        GIT_REPOSITORY https://github.com/EndstoneMC/endstone.git
        GIT_TAG main
)
FetchContent_MakeAvailable(endstone)

if (NOT CMAKE_SOURCE_DIR STREQUAL PROJECT_SOURCE_DIR)
    add_library(endstone_papi INTERFACE)
    target_include_directories(endstone_papi INTERFACE include)
    target_link_libraries(endstone_papi INTERFACE endstone::endstone)
    return()
endif ()

execute_process(
        COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
        OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE pybind11_ROOT)
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_${PROJECT_NAME} endstone_papi/_papi.cpp)
target_include_directories(_${PROJECT_NAME} PRIVATE include)
target_link_libraries(_${PROJECT_NAME} PRIVATE endstone::endstone)
install(TARGETS _papi DESTINATION "endstone_papi" COMPONENT python)
install(DIRECTORY include/ DESTINATION "endstone_papi/include" COMPONENT python)

add_subdirectory(examples/cpp)
