cmake_minimum_required(VERSION 3.5)
project(Parts_1_2)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp gauss.h newton.h solver_1_2.h ../consts/consts.h)
add_executable(Parts_1_2 ${SOURCE_FILES})