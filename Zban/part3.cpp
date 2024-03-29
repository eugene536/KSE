#include <bits/stdc++.h>
#include "../consts/consts.h"


using namespace std;

typedef double dbl;
//#define double long double

const int S = 6;
const string HCl = "HCl";
const string AlCl3 = "AlCl3";
const string GaCl = "GaCl";
const string NH3 = "NH3";
const string H2 = "H2";
const string N2 = "N2";
const string x = "x";
const string substs[] = { HCl, AlCl3, GaCl, NH3, H2, N2 };
const double EPS = 1e-9;

string inttostr(int x) {
    stringstream ss;
    string s;
    ss << x;
    ss >> s;
    return s;
}
vector<double> f(vector<pair<string, double> > v) {
    vector<double> res(S + 1, 0.0);
    for (auto o : v) {
        int id = find(substs, substs + S, o.first) - substs;
        assert(id < S || o.first == "");
        res[id] = o.second;
    }
    return res;
}

void print(vector<double> a) {
    for (int i = 0; i < (int)a.size(); i++) cerr << (dbl)a[i] << " ";
    cerr << endl;
}

void print(vector<vector<double> > a) {
    for (int i = 0; i < (int)a.size(); i++) {
        print(a[i]);
    }
}

// solve gauss for non singular nxn matrix
vector<double> gauss(vector<vector<double> > a) {
    int n = a.size();
    for (int i = 0; i < n; i++) assert(a[i].size() == n + 1);

    for (int i = 0; i < n; i++) {
        int mx = i;
        for (int j = i; j < n; j++) {
            if (fabs(a[j][i]) > fabs(a[mx][i])) {
                mx = j;
            }
        }
        if (fabs(a[mx][i]) < EPS) {
            //assert(0);
        }
        swap(a[i], a[mx]);
        for (int j = 0; j < n; j++) if (j != i) {
            double coef = a[j][i] / a[i][i];
            for (int k = 0; k <= n; k++) {
                a[j][k] -= a[i][k] * coef;   
            }
        }
    }
    vector<double> res(n);
    for (int i = 0; i < n; i++) res[i] = a[i][n] / a[i][i];
    return res;
}

const string variables[] = { HCl, AlCl3, GaCl, NH3, H2, x };
// 16, 17, 19, 18, 15, 14


int ttest = 0;
int test = 0;
void solve(vector<vector<double> > a, double delta, double T) {
    ttest++;
    test = 0;
    a.push_back(f({{HCl, 1.0}}));
    a.push_back(f({{AlCl3, 1.0}, {GaCl, 1.0}, {"", 30.0}}));
    a.push_back(f({{NH3, 1.0}, {"", 1500}}));
    a.push_back(f({{H2, 1.0}, {N2, 1.0}, {"", 98470}}));

    vector<double> res_x_g;
    vector<double> res_x;
    map<string, vector<double> > res_G;
    vector<double> res_valgan;
    for (double x_g = 0.1; x_g < 0.95; x_g += 0.01) {
        vector<vector<double> > na = a;
        na.push_back(f({{AlCl3, x_g - 1}, {GaCl, x_g}}));

        vector<double> pGName = gauss(na);

        map<string, double> D;
        map<string, double> P_g;
        for (int i = 0; i < S; i++) {
            P_g[substs[i]] = pGName[i];
        }
        for (int i = 0; i < 5; i++) {
            D[variables[i]] = consts::get_D(variables[i], T);
        }
        double K9 = consts::get_K(9, T);
        double K10 = consts::get_K(10, T);
        cerr << "K9 K10 " << (dbl)K9 << " " << (dbl)K10 << endl;
        auto F = [&](vector<double> xx) {
            map<string, double> P_e;
            double x = xx[5];
            for (int i = 0; i < 5; i++) {
                P_e[variables[i]] = xx[i];
            }
            vector<double> nx(6);
            nx[0] = D[HCl] * (P_g[HCl] - P_e[HCl]) + 2 * D[H2] * (P_g[H2] - P_e[H2]) + 3 * D[NH3] * (P_g[NH3] - P_e[NH3]);
            nx[1] = 3 * D[AlCl3] * (P_g[AlCl3] - P_e[AlCl3]) + D[GaCl] * (P_g[GaCl] - P_e[GaCl]) + D[HCl] * (P_g[HCl] - P_e[HCl]);
            nx[2] = D[AlCl3] * (P_g[AlCl3] - P_e[AlCl3]) * (1 - x) - D[GaCl] * (P_g[GaCl] - P_e[GaCl]) * x;
            nx[3] = D[AlCl3] * (P_g[AlCl3] - P_e[AlCl3]) + D[GaCl] * (P_g[GaCl] - P_e[GaCl]) - D[NH3] * (P_g[NH3] - P_e[NH3]);
            nx[4] = P_e[GaCl] * P_e[NH3] - K10 * (1 - x) * P_e[HCl] * P_e[H2];
            nx[5] = P_e[AlCl3] * P_e[NH3] - K9 * x * pow(P_e[HCl], 3);
//            nx[5] = min(nx[5], (double)1);
//            nx[5] = max(nx[5], (double)0);
            return nx;
        };
        vector<double> cx(6, 1.0);
        for (int i = 0; i < 5; i++) cx[i] = max(P_g[variables[i]] + 1.0, (double)1.0);
        cx[5] = 0.5;
        //cx.assign(6, 1.0);
        //cx[5] = x_g;
        //cx[0] = 10;
        //cx[3] = 1000;
        cx[0] = 19.269117954186658;
        cx[1] = 4.5960254796512426E-8;
        cx[2] = 11.559631023363089;
        cx[3] = 1489.378322244069;
        cx[4] = 9849.572521125578;
        cx[5] = 0.308603454760525;

        int n = 6;
        int iters = 1;
        print(cx);
//const string variables[] = { HCl, AlCl3, GaCl, NH3, H2, x };
        for (;; iters++) {
            map<string, double> P_e;
            double x = cx[5];
            for (int i = 0; i < 5; i++) {
                P_e[variables[i]] = cx[i];
            }
            vector<vector<double> > w(n, vector<double>(n, 0.0));
            w[0][0] = -D[HCl]; w[0][4] = -2 * D[H2]; w[0][3] = -3 * D[NH3];
            w[1][1] = -3 * D[AlCl3]; w[1][2] = -D[GaCl]; w[1][0] = -D[HCl];
            w[2][1] = -D[AlCl3] * (1 - x); w[2][2] = D[GaCl] * x; w[2][5] = -D[AlCl3] * (P_g[AlCl3] - P_e[AlCl3]) - D[GaCl] * (P_g[GaCl] - P_e[GaCl]);
            w[3][1] = -D[AlCl3]; w[3][2] = -D[GaCl]; w[3][3] = D[NH3];
            w[4][2] = P_e[NH3]; w[4][3] = P_e[GaCl]; w[4][5] = -K10 * -P_e[HCl] * P_e[H2]; w[4][0] = -K10 * (1 - x) * P_e[H2]; w[4][4] = -K10 * (1 - x) * P_e[HCl];
            w[5][1] = P_e[NH3]; w[5][3] = P_e[AlCl3]; w[5][5] = -K9 * pow(P_e[HCl], 3); w[5][0] = -K9 * x * 3 * pow(P_e[HCl], 2);

            
            vector<double> rx = F(cx);
            for (int i = 0; i < n ;i++) {
                w[i].push_back(-rx[i]);
            }
            //print(w);
            vector<double> dx = gauss(w);
            double mx = 0.0;
            for (int i = 0; i < n; i++) {
                cx[i] += dx[i];
                mx = max(mx, fabs(dx[i]));
            }
            //cx[5] = max(cx[5], (double)0); cx[5] = min(cx[5], (double)1);
            print(cx);
            if (mx < 1e-9) break;
        }
        cerr << "x^g " << (dbl)x_g << " simple iterations finished with " << iters << " iterations" << endl;
        double x = cx[5];
        res_x_g.push_back(x_g);
        res_x.push_back(x);
        map<string, double> P_e;
        for (int i = 0; i < 5; i++) {
            P_e[variables[i]] = cx[i];
        }

        map<string, double> GG;
        for (auto it : P_e) {
            string name = it.first;
            double G = D[name] * (P_g[name] - P_e[name]) / (8314 * T * delta);
            GG[name] = G;
            res_G[name].push_back(G);
        }

        double val = (GG[AlCl3] * (consts::get_mu("AlN", T) / 3200) + GG[GaCl] * (consts::get_mu("GaN", T) / 6150)) * 1e9;
        res_valgan.push_back(val);
    }

    string out = "out" + inttostr(ttest);
    freopen((out + inttostr(++test)).c_str(), "w", stdout);
    for (int i = 0; i < (int)res_x_g.size(); i++) {
        cout << (dbl)res_x_g[i] << " \n"[i + 1 == (int)res_x_g.size()];
    }
    for (int i = 0; i < (int)res_x.size(); i++) {
        cout << (dbl)res_x[i] << " \n"[i + 1 == (int)res_x.size()];
    }

    freopen((out + inttostr(++test)).c_str(), "w", stdout);
    for (int i = 0; i < (int)res_x_g.size(); i++) {
        cout << (dbl)res_x_g[i] << " \n"[i + 1 == (int)res_x_g.size()];
    }
    for (int i = 0; i < (int)res_x.size(); i++) {
        cout << (dbl)res_valgan[i] << " \n"[i + 1 == (int)res_x.size()];
    }

    for (auto it : res_G) {
        freopen((out + inttostr(++test)).c_str(), "w", stdout);
        for (int i = 0; i < (int)res_x_g.size(); i++) {
            cout << (dbl)res_x_g[i] << " \n"[i + 1 == (int)res_x_g.size()];
        }
        for (int i = 0; i < (int)it.second.size(); i++) {
            cout << (dbl)it.second[i] << " \n"[i + 1 == (int)it.second.size()];
        }
        cout << "part " << ttest << ": G[" << it.first << "]" << endl;

   }
}


int main() {
    cerr.precision(10);
    cerr << fixed;
    cout.precision(10);
    cout << fixed;

    vector<vector<double> > a;

    auto a1 = a;
    a1.push_back(f({{H2, 1.0}}));

    auto a2 = a;
    a2.push_back(f({{H2, 9.0}, {N2, -1.0}}));

    solve(a1, 0.01, 1100 + 273.15);
    cerr << endl;
    solve(a2, 0.01, 1100 + 273.15);
}
