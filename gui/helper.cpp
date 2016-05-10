 #include <bits/stdc++.h>
 #include <stdlib.h>
 
std::ofstream log_err("/dev/null");
#define cerr log_err
#include "../belonogov/solver_1_2.h"
#undef cerr

using namespace std;

const vector<string> elements {"Ga", "Al"};

struct DummyClass {
public:
    double getValue(string const &, int) {
        return rand() % 300 - (rand() % 10 * 1.) / 1000;
    }
};

map<string, vector<string>> queries
    {{"Al", {"AlCl", "AlCl2", "AlCl3", "V"}},
     {"Ga", {"GaCl", "GaCl2", "GaCl3", "V"}}};

void draw_1_2(string const & name, int const minT, int const maxT) {
    vector<int> temp;
    generate_n(back_inserter(temp), ((maxT - minT + 1) / 3), 
        [&minT]() { 
            static int v = minT;
            v += 3;
            return v;
        }
    );
    
    parts_1_2::Solver solver_1_2;
    vector<string> const & types = queries[name];

    for (auto type: types) {
        vector<double> ys;
        transform(temp.begin(), temp.end(), back_inserter(ys), 
            [&solver_1_2, &name, &type] (int x) -> double {
                //cerr << name << " " << type << " " << x << endl;
                return log(abs(solver_1_2.get(name, type, x))) - 1;
            }
        );


        stringstream ss;
        for (int x: temp) 
            ss << x << " ";
        ss << "\n";
        for (double y: ys)
            ss << fixed << setprecision(3) << y << " ";
        ss << "\n";
        cerr << ss.str() << endl;

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

int main() {
    //parts_1_2::Solver solver_1_2;
    //cerr << solver_1_2.get("Ga", "GaCl", 652) << endl;
    //return 0;

    map<string, pair<int, int>> ranges
        {{"Al", {350, 650}},
         {"Ga", {650, 950}}};

    for (string const & element: elements) {
        draw_1_2(element, ranges[element].first, ranges[element].second);
    }

    return 0;
}
