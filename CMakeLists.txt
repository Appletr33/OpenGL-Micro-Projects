cmake_minimum_required(VERSION 3.19)
project(OpenGLearning)

set(CMAKE_CXX_STANDARD 11)
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY "/Users/alexander/CLionProjects/OpenGLearning/Camera_Test/build")

IF(CMAKE_BUILD_TYPE MATCHES Release)
    message("Emscripten mode")
    set(CMAKE_EXECUTABLE_SUFFIX "1.html")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}-s USE_GLFW=3 -s LEGACY_GL_EMULATION=0 -s FULL_ES3=1 -s MIN_WEBGL_VERSION=3 -s MAX_WEBGL_VERSION=3 --preload-file ../Camera_Test/build/resources") #-g3
ELSE()
ENDIF(CMAKE_BUILD_TYPE MATCHES Release)

include_directories(/usr/local/include)
include_directories(/usr/local/Cellar/glad/include/)

set(GLFW_LINK /usr/local/lib/libglfw.3.3.dylib)
link_libraries(${OPENGL} ${GLFW_LINK})


add_executable(OpenGLearning Camera_Test/src/camera.cpp includes/glad.c)

