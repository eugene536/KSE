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

    inline void printMat(vector < vector < double > > data) {
        int n = data.size();
        cerr.precision(17);
        cerr << fixed;
        cerr << "==================\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double x = data[i][j];
                if (abs(x) < 1e-9)
                    x = 0;
                cerr << x << " ";
            }
            cerr << ": " << data[i][n] << endl;
        }
        cerr << "==================\n";
    }



    inline vector<double> gauss(vector<vector<double> > data) {
        int n = data.size();
        assert((int) data[0].size() == n + 1);
        //printMat(data);
        //exit(0);
        for (int i = 0; i < n; i++) {
            int cur = i;
            for (int j = i; j < n; j++)
                if (abs(data[cur][i]) < abs(data[j][i]))
                    cur = j;
            for (int j = 0; j <= n; j++)
                swap(data[cur][j], data[i][j]);
            double cof = data[i][i];
            assert(abs(cof) > 1e-30);
            for (int j = 0; j <= n; j++)
                data[i][j] /= cof;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                double cof = data[j][i];
                for (int k = 0; k <= n; k++)
                    data[j][k] -= cof * data[i][k];
            }
        }
        vector<double> res;
        for (int i = 0; i < n; i++)
            res.push_back(data[i][n]);
        return res;
    }

}


#endif //PARTS_1_2_GAUSS_H
