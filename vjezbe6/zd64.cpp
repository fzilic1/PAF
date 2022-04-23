#include <iostream>

void solve(float a1, float b1, float c1, float a2, float b2, float c2){
    float y=(c2-(a2/a1)*c1)/(b2-(a2/a1)*b1);
    float x=(c1-b1*y)/a1;
    std::cout << x << " " << y;
}

int main(){
    solve(3, 2, -1, 5, 1, 6);
    return 0;
}