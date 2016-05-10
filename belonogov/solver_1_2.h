//
// Created by vanya on 09.05.16.
//

#ifndef PARTS_1_2_SOLVER_1_2_H
#define PARTS_1_2_SOLVER_1_2_H


#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>
#include <map>

#undef NDEBUG

#include <cassert>
#include "newton.h"
#include "../consts/consts.h"
#include "main.h"


using namespace std;


namespace parts_1_2 {
    inline bool equal(double a, double b) {
        return fabs(a - b) < 1e-9;
    }

    struct Solver {
        double curTemp = -1;
        string curType;
        map<string, int> id;


        vector<double> G;
        double VType;

        int getId(string s) {
            assert(id.count(s) == 1);
            return id[s];
        }

        shared_ptr<Expression> makeVar(double cof, int deg, int id) {
            return shared_ptr<Expression>(new Variable(cof, deg, id));
        }

        void solve(string type, double temp) {
            id.clear();
            const int n = 5;
            vector<shared_ptr<Expression> > f(n);
            id[type + "Cl"] = 0;
            id[type + "Cl2"] = 1;
            id[type + "Cl3"] = 2;
            id["HCl"] = 3;
            id["H2"] = 4;
            id["N2"] = 5;

            int shift = (type == "Al") ? 0 : 3;
            double K_1 = consts::get_K(1 + shift, temp);
            double K_2 = consts::get_K(2 + shift, temp);
            double K_3 = consts::get_K(3 + shift, temp);


            db3(K_1, K_2, K_3);

            vector<double> D(n);

            D[getId("HCl")] = consts::get_D("HCl", temp);
            D[getId("H2")] = consts::get_D("H2", temp);
            D[getId(type + "Cl")] = consts::get_D(type + "Cl", temp);
            D[getId(type + "Cl2")] = consts::get_D(type + "Cl2", temp);
            D[getId(type + "Cl3")] = consts::get_D(type + "Cl3", temp);

            cerr << "D: ";
            for (auto x: D)
                cerr << x << " ";
            cerr << endl;

            //exit(0);


//            double D[getId("HCl")] = consts::get_D("HCl", temp);
//            double D_H2 = consts::get_D("H2", temp);
//            double D[getId(type + "Cl")] = consts::get_D(type + "Cl", temp);
//            double D[getId(type + "Cl")]2 = consts::get_D(type + "Cl2", temp);
//            double D[getId(type + "Cl")]3 = consts::get_D(type + "Cl3", temp);



            f[0] = shared_ptr<Expression>(new Addition({
                                                               makeVar(1, 2, getId("HCl")),
                                                               shared_ptr<Expression>(new Multiplication(
                                                                       makeVar(-K_1, 2, getId(type + "Cl")),
                                                                       makeVar(1, 1, getId("H2"))
                                                               ))}));

            f[1] = shared_ptr<Expression>(new Addition({
                                                               makeVar(1, 2, getId("HCl")),
                                                               shared_ptr<Expression>(new Multiplication(
                                                                       makeVar(-K_2, 1, getId(type + "Cl2")),
                                                                       makeVar(1, 1, getId("H2"))
                                                               ))}));


            f[2] = shared_ptr<Expression>(new Addition({
                                                               makeVar(1, 6, getId("HCl")),
                                                               shared_ptr<Expression>(new Multiplication(
                                                                       makeVar(-K_3, 2, getId(type + "Cl3")),
                                                                       makeVar(1, 3, getId("H2"))
                                                               ))}
                                          )
            );

            vector<double> Pg(n + 1);
            Pg[getId("HCl")] = 1e4;
            Pg[getId("N2")] = 9e4;
            Pg[getId(type + "Cl")] = 0;
            Pg[getId(type + "Cl2")] = 0;
            Pg[getId(type + "Cl3")] = 0;
            Pg[getId("H2")] = 0;

            f[3] = shared_ptr<Expression>(new Addition({
//                                                shared_ptr < Expression >(Variable(D[getId(type + "Cl")] * P_g_HCl, 0, -1)),
                                                               makeVar(D[getId("HCl")] * Pg[getId("HCl")], 0, -1),
                                                               makeVar(-D[getId("HCl")], 1, getId("HCl")),
                                                               makeVar(-2 * D[getId("H2")], 1, getId("H2"))}
            ));

            f[4] = shared_ptr<Expression>(new Addition({
                                                               makeVar(-D[getId(type + "Cl")], 1, getId(type + "Cl")),
                                                               makeVar(-2 * D[getId(type + "Cl2")], 1, getId(type + "Cl2")),
                                                               makeVar(-3 * D[getId(type + "Cl3")], 1, getId(type + "Cl3")),
//                                                shared_ptr < Expression >(Variable(D[getId("HCl")] * P_g_HCl, 0, -1)),
                                                               makeVar(D[getId("HCl")] * Pg[getId("HCl")], 0, -1),
                                                               makeVar(-D[getId("HCl")], 1, getId("HCl"))
                                                       }
            ));

            vector<double> start;
            for (int i = 0; i < n; i++)
                start.push_back(rand() % 10);
            auto Pe = newton(start, f);

            G.resize(n);
            const double R = 8314;
            const double delta = 0.01;
            for (int i = 0; i < n; i++)
                G[i] = D[i] * (Pg[i] - Pe[i]) / (R * temp * delta);

            double cofType;
            if (type == "Al")
                cofType = 26.9815386 / 2698.9;
            else
                cofType = 69.723 / 5910;

            VType = (G[getId(type + "Cl")] + G[getId(type + "Cl2")] + G[getId(type + "Cl3")]) * cofType * 1e9;


            curType = type;
            curTemp = temp;
        }

        // ex: get("Al", "AlCl2", 30);
        //     get("Al", "V", 30);
        double get(const string & type, const string & name, double temp) {
            if (type != "Al" && type != "Ga")
                throw logic_error("expected Al or Ga found: " + type);
            if (!equal(curTemp, temp) || curType != type) {
                solve(type, temp);
            }
            if (name == "V")
                return VType;
            return G[getId(name)];
        }
    };
}


#endif //PARTS_1_2_SOLVER_1_2_H
