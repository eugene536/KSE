#ifndef CONSTS_H_
#define CONSTS_H_

#include <cmath>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
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

static const std::string const_data_value(
"14 "
"AlCl                  51032.    318.9948      36.94626   -0.001226431  1.1881743       5.638541       -5.066135        5.219347    62.4345    3.58     932.   "
"AlCl2               -259000.    427.2137      56.56409   -0.002961273  1.893842       12.40072       -22.65441        21.29898     97.8875    5.3      825. "
"AlCl3               -584100.    511.8114      81.15042   -0.004834879  2.752097       13.40078       -21.28001        16.92868    133.3405    5.13     472. "
"GaCl                 -70553.    332.2718      37.11052   -0.000746187  1.1606512       4.891346       -4.467591        5.506236   105.173     3.696    348.2 "
"GaCl2               -241238.    443.2976      57.745845  -0.002265112  1.8755545       3.66186        -9.356338       15.88245    140.626     4.293    465.  "
"GaCl3               -431573.    526.8113      82.03355   -0.003486473  2.6855923       8.278878      -14.5678         12.8899     176.080     5.034    548.2 "
"NH3                  -45940.    231.1183      20.52222    0.000716251  0.7677236     244.6296       -251.69          146.6947      17.031     3.0      300.  "
"H2                        0.    205.5368      29.50487    0.000168424  0.86065612    -14.95312        78.18955       -82.78981      2.016     2.93      34.1 "
"HCl                  -92310.    243.9878      23.15984    0.001819985  0.6147384      51.16604       -36.89502         9.174252    36.461     2.737    167.1 "
"N2                        0.    242.8156      21.47467    0.001748786  0.5910039      81.08497      -103.6265         71.30775     28.0135    3.798     71.4 "
"Al                        0.    172.8289      50.51806   -0.00411847   1.476107     -458.1279       2105.75        -4168.337       26.9815    0         0 "
"Ga                        0.    125.9597      26.03107    0.001178297  0.13976        -0.5698425       0.04723008      7.212525    69.723     0          0     "
"AlN                 -319000.    123.1132      44.98092   -0.00734504   1.86107        31.39626       -49.92139        81.22038     40.988     0          0     "
"GaN                 -114000.    160.2647      52.86351   -0.00799055   2.113389        1.313428       -2.441129        1.945731    83.730     0          0     "
);

inline double x_on_temp(double temp) {
    return temp / 10000.0;
}

inline void update_map(std::map<std::string, std::map<std::string, double> >& segal_consts) {
    if (segal_consts.empty()) {
			  std::stringstream fin(const_data_value);
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
    double F = cur["phi1"] 
						 	 + cur["phi2"] * log(x_on_temp(temp)) 
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
    double ans = 0.02628 * std::pow(temp, 1.5) / 
        (atmosphere_pressure 
         * ((segal_consts[name]["sigma"] + segal_consts["N2"]["sigma"]) / 2)
         * (1.074 * std::pow(temp /  std::pow(segal_consts[name]["epsil"] * segal_consts["N2"]["epsil"], 0.5), -0.1604))
         * (2 * segal_consts[name]["mu"] * segal_consts["N2"]["mu"] / (segal_consts[name]["mu"] + segal_consts["N2"]["mu"]))
        );
    return ans;
}

}

#endif
