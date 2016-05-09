//
// Created by vanya on 09.05.16.
//

#ifndef PARTS_1_2_GAUSS_H
#define PARTS_1_2_GAUSS_H

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

using namespace std;

namespace parts_1_2 {

    inline vector<double> gauss(vector<vector<double> > b) {
        int n = b.size();
        assert((int) b[0].size() == n + 1);
        for (int i = 0; i < n; i++) {
            int cur = i;
            for (int j = i; j < n; j++)
                if (abs(b[cur][i]) < abs(b[j][i]))
                    cur = j;
            for (int j = 0; j <= n; j++)
                swap(b[cur][j], b[i][j]);
            double cof = b[i][i];
            assert(abs(cof) > 1e-9);
            for (int j = 0; j <= n; j++)
                b[i][j] /= cof;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                double cof = b[j][i];
                for (int k = 0; k <= n; k++)
                    b[j][k] -= cof * b[i][k];
            }
        }
        vector<double> res;
        for (int i = 0; i < n; i++)
            res.push_back(b[i][n]);
        return res;
    }

}


#endif //PARTS_1_2_GAUSS_H
