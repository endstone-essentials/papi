cmake_minimum_required(VERSION 3.15)

project(papi_example CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
        endstone_papi
        GIT_REPOSITORY https://github.com/endstone-essentials/papi.git
        GIT_TAG main
)
FetchContent_MakeAvailable(endstone endstone_papi)

endstone_add_plugin(${PROJECT_NAME} plugin.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE endstone_papi)
