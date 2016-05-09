//
// Created by vanya on 09.05.16.
//

#ifndef PARTS_1_2_NEWTON_H
#define PARTS_1_2_NEWTON_H

#include <vector>

using namespace std;

namespace parts_1_2 {

    struct Monom {
        double cof;
        int deg;
        Monom(double cof, int deg) : cof(cof), deg(deg) { }
        double operator () (double x) {
            double res = 1;
            for (int i = 0; i < deg; i++)
                res *= x;
            res *= cof;
            return res;
        }
        Monom derivative() {
            return Monom(cof * deg, deg - 1);
        }
    };

    vector < double > newton(vector < double > point, vector < vector < Monom > > f) {
        int n = point.size();


    }
}


#endif //PARTS_1_2_NEWTON_H
