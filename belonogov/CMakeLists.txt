cmake_minimum_required(VERSION 3.2)
project(Parts_1_2)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")



#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "/home/vanya/Documents/prog/KSE/KSE/belonogov/build")

set(SOURCE_FILES main.cpp gauss.h newton.h solver_1_2.h ../consts/consts.h main.h)
add_executable(Parts_1_2 ${SOURCE_FILES})


