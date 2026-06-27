# Install script for directory: /home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/V2X_Integration/msg" TYPE FILE FILES
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration/msg/BSM.msg"
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration/msg/ESP_21_Msg.msg"
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration/msg/FB_05_Msg.msg"
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration/msg/SARA_06_Msg.msg"
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration/msg/V2X_Warning.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/V2X_Integration/cmake" TYPE FILE FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/V2X_Integration-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/devel/include/V2X_Integration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/devel/share/roseus/ros/V2X_Integration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/devel/share/common-lisp/ros/V2X_Integration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/devel/share/gennodejs/ros/V2X_Integration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/devel/lib/python2.7/dist-packages/V2X_Integration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/devel/lib/python2.7/dist-packages/V2X_Integration")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/V2X_Integration" TYPE PROGRAM FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/v2x_function.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/V2X_Integration" TYPE PROGRAM FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/jupiter_twins.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/V2X_Integration" TYPE PROGRAM FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/v2x_signal.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/V2X_Integration.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/V2X_Integration/cmake" TYPE FILE FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/V2X_Integration-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/V2X_Integration/cmake" TYPE FILE FILES
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/V2X_IntegrationConfig.cmake"
    "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/build/V2X_Integration/catkin_generated/installspace/V2X_IntegrationConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/V2X_Integration" TYPE FILE FILES "/home/carla/Documents/AlbertYao/V2X_demo/catkin_ws/src/V2X_Integration/package.xml")
endif()

