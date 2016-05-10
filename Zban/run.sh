g++ part3.cpp -o part3 --std=c++14 
./part3
./../gui/log_plot.py --yName "x(x_g), P_g_H2=0" --xName "x_g" < out11 &
./../gui/log_plot.py --yName "V_algan(x_g), P_g_H2=0" --xName "x_g" < out12 &
./../gui/log_plot.py --yName "x(x_g), P_g_H2=1/9P_g_N2" --xName "x_g" < out21 &
./../gui/log_plot.py --yName "V_algan(x_g), P_g_H2=1/9P_g_N2" --xName "x_g" < out22 &
