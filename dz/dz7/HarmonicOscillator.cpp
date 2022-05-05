#include <HarmonicOscillator.h>
#include <math.h>
#include <fstream>

using namespace std;

HarmonicOscillator::HarmonicOscillator(double x0, double v0, double ki, double mi, double step){
    t=0;
    dt=step;
    x=x0;
    v=v0;
    k=ki;
    m=mi;
    a=-k*x/m;
}

HarmonicOscillator::~HarmonicOscillator(){

}

void HarmonicOscillator::move(){
    a=-k*x/m;
    v+=a*dt;
    x+=v*dt;
    t+=dt;
}

void HarmonicOscillator::oscillate(double to){
    ofstream outfile;
    outfile.open("podatci.txt");
    while(t < to){
        move();
        outfile << t << " " << x << " " << v << " " << a << endl;   
    }
    outfile.close();
    }

double HarmonicOscillator::period(){
    double T=0;

    double t_0=t;
    double x_0=x;
    double v_0=v;
    double a_0=a;

    move();
    if(x >= 0){
        while(abs(x) == x){
            move();}
        while(abs(x) != x){
            move();
            T+=dt;}
        }
    else if(x < 0){
        while(abs(x) != x){
            move();}
        while(abs(x) == x){
            move();
            T+=dt;}
    }

    t=t_0;
    x=x_0;
    v=v_0;
    a=a_0;

    return(2*T);
}