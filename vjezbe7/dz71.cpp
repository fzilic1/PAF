#include <HarmonicOscillator.h>
#include <iostream>

using namespace std;

int main(){
    HarmonicOscillator o1(6, 0, 4, 2, 0.01);
    double T=o1.period();
    o1.oscillate(T);

    return 0;
}