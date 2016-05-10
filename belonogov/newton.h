//
// Created by vanya on 09.05.16.
//

#ifndef PARTS_1_2_NEWTON_H
#define PARTS_1_2_NEWTON_H

#include <vector>
#include <memory>
#include "gauss.h"
#include "main.h"

using namespace std;

namespace parts_1_2 {

    struct Expression {
        virtual double value(vector < double > point) = 0;
        virtual double derivative(vector < double > point, int id) = 0;

        virtual ~Expression() { }
    };

    struct Addition : Expression {
        vector < shared_ptr < Expression > > ch;

        Addition(const vector<shared_ptr<Expression>> &ch) : ch(ch) { }

        double value(vector < double > point) override {
            double res = 0;
            for (auto v: ch)
                res += v->value(point);
            return res;
        }

        double derivative(vector < double > point, int id) override {
            double res = 0;
            for (auto v: ch)
                res += v->derivative(point, id);
            return res;
        }
    };

    struct Multiplication: Expression {
        shared_ptr < Expression > l, r;

        Multiplication(const shared_ptr<Expression> &l, const shared_ptr<Expression> &r) : l(l) , r(r) { }

        double value(vector < double > point) override {
            return l->value(point) * r->value(point);
        }

        double derivative(vector < double > point, int id) override {
            return l->value(point) * r->derivative(point, id) + l->derivative(point, id) + r->value(point);
        }
    };

    struct Variable : Expression {
        double cof;
        int deg, varId;

        Variable(double cof, int deg, int varId) : cof(cof), deg(deg), varId(varId) { }

        double value(vector < double > point) override {
            double res = 1;
            for (int i = 0; i < deg; i++) {
                assert(varId != -1);
                res *= point[varId];
            }
            return res * cof;
        }

        double derivative(vector < double > point, int id) override {
            if (id != varId)
                return 0;
            double res = 1;
            for (int i = 0; i < deg - 1; i++)
                res *= point[varId];
            return res * cof * deg;
        }
    };


    inline vector < double > newton(vector < double > point, vector < shared_ptr < Expression > > f) {
        int n = point.size();

        bool converge = 0;
        for (int it = 0; it < 100; it++) {
            vector < vector < double > > data(n, vector < double > (n + 1));
            for (int i = 0; i < n; i++) {
                data[i][n] += - f[i]->value(point);
                for (int j = 0; j < n; j++) {
                    double der = f[i]->derivative(point, j);
                    data[i][j] += der;
                    data[i][n] += der * point[j];
                }
            }
            auto prev = point;
            point = gauss(data);
            double mxDiff = 0;
            double mx = point[0];
            for (int i = 0; i < (int)point.size(); i++)
                mxDiff = max(abs(point[i] - prev[i]), mxDiff);
            for (auto x: point)
                mx = max(mx, x);

            if (mxDiff < max(1.0, abs(mx)) * 1e-6) {
                converge = 1;
                db("Converge");
                break;
            }
            /*db3(it, mxDiff, mx);
            for (auto x: point)
                cerr << x << " ";
            cerr << endl;*/
        }
        if (!converge)
            db("NOT Converge");
        return point;
    }
}


#endif //PARTS_1_2_NEWTON_H
