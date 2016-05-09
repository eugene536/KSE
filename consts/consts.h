#ifndef CONSTS_H_
#define CONSTS_H_

#include <cmath>
#include <string>
#include <map>
#include <fstream>
#include <iostream>

namespace consts {

/* 
   number - number of constant(reaction)
   temp - temperature in kelvin
   return K - const equilibrium reactions ("ravnovesiya reaktsiy")
*/
inline double get_K(int number, int temp);

/* 
   name - name of substance, "AlCl3", "N2", "Al"
   temp - temperature in kelvin
   return const D - diffusion coefficient
*/
inline double get_D(const std::string& name, int temp);

static const double R_kmol = 8.314;
static const int atmosphere_pressure = 100000;

/* *****************
    some math
*/
inline double x_on_temp(double temp) {
    return temp / 10000.0;
}

inline void update_map(std::map<std::string, std::map<std::string, double> >& segal_consts) {
    if (segal_consts.empty()) {
        std::ifstream fin("bank_td_fragment.dat");
        int n;
        fin >> n;
        std::string phi = "phi";
        for (int lp = 0; lp < n; lp++) {
            std::string subst_name;
            double value;
            fin >> subst_name;
            segal_consts.insert(std::make_pair(subst_name, std::map<std::string, double>()));
            fin >> value;
            segal_consts[subst_name].insert(make_pair(std::string("H"), value));
            for (int i = 1; i < 8; i++) {
                fin >> value;
                segal_consts[subst_name].insert(make_pair(phi + std::to_string(i), value));
            }
            fin >> value;
            segal_consts[subst_name].insert(make_pair(std::string("mu"), value));
            fin >> value;
            segal_consts[subst_name].insert(make_pair(std::string("sigma"), value));
            fin >> value;
            segal_consts[subst_name].insert(make_pair(std::string("epsil"), value));
        }
    }
}

inline double get_g(const std::string& name, double temp) {
    static std::map<std::string, std::map<std::string, double> > segal_consts;
    update_map(segal_consts);
    if (segal_consts.find(name) == segal_consts.end()) {
        throw std::logic_error("unknown constant " + name);
    }
    auto cur = segal_consts.find(name)->second;
    double F = cur["phi1"] + cur["phi2"] * log(x_on_temp(temp)) 
               + cur["phi3"] / std::pow(x_on_temp(temp), 2)
               + cur["phi4"] / x_on_temp(temp)
               + cur["phi5"] * x_on_temp(temp)
               + cur["phi6"] * std::pow(x_on_temp(temp), 2)
               + cur["phi7"] * std::pow(x_on_temp(temp), 3);
    return cur["H"] - F;
}

inline double get_K(int number, int temp) {
    double delta_g = 0;
    switch (number) {
        case 1:
            delta_g = 2*get_g("Al", temp)   + 2*get_g("HCl", temp)  - 2*get_g("AlCl", temp) - 1*get_g("H2", temp);
            break;                
        case 2:                   
            delta_g = 1*get_g("Al", temp)   + 2*get_g("HCl", temp)  - 1*get_g("AlCl2", temp)- 1*get_g("H2", temp);
            break;                
        case 3:                   
            delta_g = 2*get_g("Al", temp)   + 6*get_g("HCl", temp)  - 2*get_g("AlCl3", temp)- 3*get_g("H2", temp);
            break;                
        case 4:                   
            delta_g = 2*get_g("Ga", temp)   + 2*get_g("HCl", temp)  - 2*get_g("GaCl", temp)- 1*get_g("H2", temp);
            break;                
        case 5:
            delta_g = 1*get_g("Ga", temp)   + 2*get_g("HCl", temp)  - 1*get_g("GaCl2", temp)- 1*get_g("H2", temp);
            break;                
        case 6:
            delta_g = 2*get_g("Ga", temp)   + 6*get_g("HCl", temp)  - 2*get_g("GaCl3", temp)- 3*get_g("H2", temp);
            break;                
        case 7:
            delta_g = 1*get_g("AlCl", temp)   + 1*get_g("NH3", temp)  - 1*get_g("AlN", temp) - 1*get_g("HCl", temp) - 1*get_g("H2", temp);
            break;                
        case 8:
            delta_g = 2*get_g("AlCl2", temp)  + 2*get_g("NH3", temp)  - 2*get_g("AlN", temp) - 4*get_g("HCl", temp) - 1*get_g("H2", temp);
            break;                
        case 9:
            delta_g = 1*get_g("AlCl3", temp)  + 1*get_g("NH3", temp)  - 1*get_g("AlN", temp) - 3*get_g("HCl", temp) - 0*get_g("H2", temp);
            break;                
        case 10:
            delta_g = 1*get_g("GaCl", temp)   + 1*get_g("NH3", temp)  - 1*get_g("GaN", temp) - 1*get_g("HCl", temp) - 1*get_g("H2", temp);
            break;                
        case 11:
            delta_g = 2*get_g("GaCl2", temp)  + 2*get_g("NH3", temp)  - 2*get_g("GaN", temp) - 4*get_g("HCl", temp) - 1*get_g("H2", temp);
            break;                
        case 12:
            delta_g = 1*get_g("GaCl3", temp)  + 1*get_g("NH3", temp)  - 1*get_g("GaN", temp) - 3*get_g("HCl", temp) - 0*get_g("H2", temp);
            break;                
    };
    return exp(-delta_g/(R_kmol*temp)) / atmosphere_pressure;
}

inline double get_D(const std::string& name, int temp) {
    static std::map<std::string, std::map<std::string, double> > segal_consts;
    update_map(segal_consts);
    if (segal_consts.find(name) == segal_consts.end()) {
        throw std::logic_error("unknown constant " + name);
    }
    double ans = 0.02682 * std::pow(temp, 1.5) / 
        (atmosphere_pressure 
         * ((segal_consts[name]["sigma"] + segal_consts["N2"]["sigma"]) / 2)
         * (1.074 * std::pow(temp /  std::pow(segal_consts[name]["epsil"] * segal_consts["N2"]["epsil"], 0.5), -0.1604))
         * (2 * segal_consts[name]["mu"] * segal_consts["N2"]["mu"] / (segal_consts[name]["mu"] + segal_consts["N2"]["mu"]))
        );
    return ans;
}

}

#endif
