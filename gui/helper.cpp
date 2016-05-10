 #include <bits/stdc++.h>
 #include <stdlib.h>
 
std::ofstream log_err("/dev/null");
#define cerr log_err
#include "../belonogov/solver_1_2.h"
#undef cerr

using namespace std;
 
struct DummyClass {
public:
    double getValue(string const &, int) {
        return rand() % 300 - (rand() % 10 * 1.) / 1000;
    }
};

int main() {
    vector<pair<string, vector<string>>> queries
        {{"Al", {"AlCl", "AlCl2", "AlCl3", "V"}}, 
         {"Ga", {"GaCl", "GaCl2", "GaCl3", "V"}}};

    int const kTMin = 350;
    int const kTMax = 650;

    vector<int> temp;
    generate_n(back_inserter(temp), ((kTMax - kTMin + 1) / 3), 
        [&kTMin]() { 
            static int v = kTMin;
            v += 3;
            return v;
        }
    );
    
    parts_1_2::Solver solver_1_2;
    for (auto query: queries) {
        string const & name = query.first;
        vector<string> const & types = query.second;

        for (auto type: types) {
            vector<double> ys;
            transform(temp.begin(), temp.end(), back_inserter(ys), 
                [&solver_1_2, &name, &type] (int x) -> double {
                    return log(solver_1_2.get(name, type, x)) - 1;
                }
            );

            stringstream ss;
            for (int x: temp) 
                ss << x << " ";
            ss << "\n";
            for (double y: ys)
                ss << fixed << setprecision(3) << y << " ";
            ss << "\n";

            string command = "echo \"" + ss.str() + "\" | ./log_plot.py --yName \"" + name + " (log - 1)\"";
            thread commandThread(
                [command = command.c_str()] () { 
                    system(command); 
                }
            );

            cerr << "wait closing plot" << endl;
            commandThread.join();
        }
    }

    return 0;
}
