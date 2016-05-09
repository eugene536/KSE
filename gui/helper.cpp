#include <bits/stdc++.h>
#include <stdlib.h>

using namespace std;

struct DummyClass {
public:
    double getValue(const string&, int) {
        return rand() % 300 - rand() % 200;
    }
};

int main() {
    vector<string> names{"AlCl", "AlCl2", "AlCl3"};
    const int kTMin = 350;
    const int kTMax = 650;

    vector<int> temp;
    generate_n(back_inserter(temp), ((kTMax - kTMin + 1) / 3), 
        [&kTMin]() { 
            static int v = kTMin;
            v += 3;
            return v;
        }
    );
    
    DummyClass dummy;
    for (auto name: names) {
        vector<double> ys;
        transform(temp.begin(), temp.end(), back_inserter(ys), 
            [&dummy, &name] (int x) -> double {
                return dummy.getValue(name, x);
            }
        );

        stringstream ss;
        for (int x: temp) 
            ss << x << " ";
        ss << "\n";
        for (double y: ys)
            ss << setprecision(3) << y << " ";
        ss << "\n";

        string command = "echo \"" + ss.str() + "\" | ./log_plot.py --yName " + name;
        thread commandThread(
            [command = command.c_str()] () { 
                system(command); 
            }
        );

        cerr << "wait closing plot" << endl;
        commandThread.join();
    }

    return 0;
}
