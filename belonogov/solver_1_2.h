//
// Created by vanya on 09.05.16.
//

#ifndef PARTS_1_2_SOLVER_1_2_H
#define PARTS_1_2_SOLVER_1_2_H


#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

namespace parts_1_2 {
    struct Solver {

        double get(string type, string cl_cnt) {
            if (type != "Al" && type != "Ga")
                throw logic_error("expected Al or Ga found: " + type);
            //if (type != "G" && type != )

        }
    };
}


#endif //PARTS_1_2_SOLVER_1_2_H
