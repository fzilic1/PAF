#include <Particle.h>
#include <iostream>

using namespace std;

int main(){
Particle p1(100, 45, 0, 0);
Particle p2(12, 30, 2, 11);
std::cout << p1.time() <<" ";
std::cout << p2.range();
return 0;
}