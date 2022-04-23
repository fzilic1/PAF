#include <iostream>
#include <math.h>

void kruznica(float cx, float cy, float r, float x, float y){
    float D=sqrt( pow((x-cx), 2) + pow((y-cy), 2));
    if (D < r){
        std::cout << "Tocka se nalazi unutar kruznice" << std::endl;
    }
    else if (D > r){
        std::cout << "Tocka se nalazi izvan kruznice" << std::endl;
    }
    else{
        std::cout << "Tocka se nalazi na kruznici" << std::endl;
    }
}

int main(){
    kruznica(2.4, -1.1, 5, 2, 0);
    return 0;
}