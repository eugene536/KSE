#include <iostream>
#include "solver_1_2.h"

using namespace std;
using namespace parts_1_2;


int main() {
    parts_1_2::Solver solver;

    if (1) {

        cout << solver.get("Al", "V", 823) << endl;
        cout << solver.get("Al", "AlCl", 823) << endl;
        cout << solver.get("Al", "AlCl2", 823) << endl;
        cout << solver.get("Al", "AlCl3", 823) << endl;

    }
    else {

        shared_ptr<Expression> f = shared_ptr<Expression>(new Addition({shared_ptr<Expression>(new Variable(1, 2, 0)),
                                                                        shared_ptr<Expression>(
                                                                                new Variable(-9, 0, -1))}));
        db(f->value({3}));
        db(f->value({-3}));
        //exit(0);
        auto res = newton({1}, {f});
        for (auto x: res)
            cerr << x << " ";
        cerr << endl;
    }
    return 0;
}