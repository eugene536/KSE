#include <iostream>
#include "solver_1_2.h"

using namespace std;
using namespace parts_1_2;


int main() {
    parts_1_2::Solver solver;

    if (1) {
        //db(consts::get_K(1, 823));

        //cout << solver.get("Al", "V", 823) << endl;
        cout << solver.get("Ga", "V", 950 + 273) << endl;
        cout << solver.get("Ga", "GaCl", 950 + 273) << endl;
        cout << solver.get("Ga", "GaCl2", 950 + 273) << endl;
        cout << solver.get("Ga", "GaCl3", 950 + 273) << endl;

    }
    else {



        //shared_ptr<Expression> f1 = shared_ptr<Expression>(new Addition({makeVar(1, 2, 0), makeVar(1, 2, 1), makeVar(-16, 0, -1)}));
        shared_ptr<Expression> f1 = make_shared<Multiplication>(Multiplication(
                                                make_shared < Addition > (Addition({ makeVar(1, 1, 0), makeVar(-5, 0, -1) })),
                                                make_shared < Addition > (Addition({ makeVar(1, 1, 1), makeVar(5, 0, -1) }))));

        shared_ptr<Expression> f2 = make_shared<Multiplication>(Multiplication(
                                                make_shared < Addition > (Addition({ makeVar(1, 1, 0), makeVar(2, 0, -1) })),
                                                make_shared < Addition > (Addition({ makeVar(1, 1, 1), makeVar(-3, 0, -1) }))));



        //shared_ptr<Expression> f2 = shared_ptr<Expression>(new Addition({makeVar(1, 1, 0), makeVar(1, 1, 1), makeVar(-4, 0,-1)} ));


        db(f1->value({-2, -5}));
        db(f2->value({-2, -5}));
        //exit(0);
        auto res = newton({-1000, -1000}, {f1, f2});
        for (auto x: res)
            cerr << x << " ";
        cerr << endl;



//        shared_ptr<Expression> f = shared_ptr<Expression>(new Addition({shared_ptr<Expression>(new Variable(1, 2, 0)),
//                                                                        shared_ptr<Expression>(
//                                                                                new Variable(-9, 0, -1))}));
//
//        db(f->value({3}));
//        db(f->value({-3}));
//        //exit(0);
//        auto res = newton({1}, {f});
//        for (auto x: res)
//            cerr << x << " ";
//        cerr << endl;
    }
    return 0;
}