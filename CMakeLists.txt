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
    return()
endif ()

endstone_add_plugin(${PROJECT_NAME} src/plugin.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE include)

option(PAPI_BUILD_EXAMPLE "Build the PlaceholderAPI example plugin" OFF)
if (NOT PAPI_BUILD_EXAMPLE STREQUAL OFF)
    add_subdirectory(examples/cpp)
endif ()