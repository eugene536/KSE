#ifndef CONSTS_H_
#define CONSTS_H_

#include <cmath>
#include <string>

namespace consts {

/* 
   name - name of substance, "AlCl3", "N2", "Al"
   temp - temperature in kelvin
   x - ratio of pressure of subtance to atmosphere pressure(maybe i'm wrong)
   x can be in [0, 1]
   return K - const equilibrium reactions ("ravnovesiya reaktsiy")
*/
inline double get_k(const std::string& name, double temp, double x);

/* 
   name - name of substance, "AlCl3", "N2", "Al"
   temp - temperature in kelvin
   return const D - diffusion coefficient
*/
inline double get_d(const std::string& name, double temp);

};

inline double consts::get_k(const std::string& name, double temp, double x) {
    return 1.0;
}

inline double consts::get_d(const std::string& name, double temp) {
    return 1.0;
}

#endif
