#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <functional>
#include <../consts

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = -1;
const long long INF = 1e9 + 19;

struct Gauss {
    vector < vector < double > > b;
    int n;
    Gauss(int n):n(n) {
        b.resize(n, vector < double > (n + 1, 0));
    }

    vector < double > solve() {
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
        vector < double > res;
        for (int i = 0; i < n; i++)
            res.pb(b[i][n]);
        return res;
    }
    void printMat() {
        cerr.precision(3);
        cerr << fixed;
        cerr << "==================\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double x = b[i][j];
                if (abs(x) < 1e-9)
                    x = 0;
                cerr << x << " ";
            }
            cerr << ": " << b[i][n] << endl;
        }
        cerr << "==================\n";
    }
};

struct Newton {
    vector < double > x;
    vector < function < double(vector < double >) > > f; 
    int n;
    Newton(int n):n(n) {
        x.resize(n);
        f.resize(n);
    }
};



struct BelonogovSolver_1 {

    const int MAX_TEMP = 2000;
    int curTemp = -1;
    map < string, int > id; 
    int getId(string s) {
        assert(id.count(s) == 1);
        return id[s];
    }
    double sqr(double x) {
        return x * x;
    }

    void solve(double temp) {
        id["AlCl"] = 0;
        id["AlCl2"] = 1;
        id["AlCl3"] = 2;
        id["HCl"] = 3;
        id["H2"] = 4;
        Newton newton(5);

        double K_1 = 
        newton.f[0] = [&](vector < double > x) {
            return sqr(x[getId("HCl")]) - 
        }


        curTemp = temp;
    }
    
    double get_V_al(int temp) {
        assert(0 < temp && temp < MAX_TEMP);
        if (curTemp != temp) solve(temp);

    }
    double get_G_AlCl(int temp) {
        assert(0 < temp && temp < MAX_TEMP);
        if (curTemp != temp) solve(temp);

    }
    double get_G_AlCl2(int temp) {
        assert(0 < temp && temp < MAX_TEMP);
        if (curTemp != temp) solve(temp);

    }
    double get_G_AlCl3(int temp) {
        assert(0 < temp && temp < MAX_TEMP);
        if (curTemp != temp) solve(temp);



    }
};



void read() {

}

void solve() {

}

void stress() {

}


int main(){
//#ifdef DEBUG
    freopen("input.txt", "r", stdin);
//#endif
    if (1) {
        int k = 1;
        for (int tt = 0; tt < k; tt++) {
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}





