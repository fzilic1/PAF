#include <iostream>

void pravac(float x1, float y1, float x2, float y2){
    float a=(y2-y1)/(x2-x1);
    float b=y1-a*x1;
    std::cout << "y(x)=" << a << "x+" << b << std::endl;
    }

int main(){
    pravac(1, 3.4 , 2, -2);
    return 0;
}