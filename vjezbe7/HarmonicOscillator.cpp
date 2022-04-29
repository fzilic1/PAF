#include <HarmonicOscillator.h>
#include <math.h>

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

void HarmonicOscillator::oscillate(double x0, double v0, double to){
    while(t < to){
        move();
    }
}

double HarmonicOscillator::period(){
    double xp=x;
    move();
    while(x != xp){
        move();
    }
    return(2*t);
}