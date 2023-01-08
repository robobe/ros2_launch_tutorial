cmake_minimum_required(VERSION 3.8)
project(pkg_launch_tutorial)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

install(
  DIRECTORY launch worlds pkg_launch_tutorial
  DESTINATION share/${PROJECT_NAME}
)
# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(PROGRAMS
    pkg_launch_tutorial/minimal_node.py
    DESTINATION lib/${PROJECT_NAME}
    )

ament_package()
