#include <iostream>

void interval(int list[], int a, int b){
    int s=list.size();
    for(int i=0; i<=s; i++){
        if (list[i] >= a && list[i] <= b){
            std::cout << list[i] <<std::endl;
        }
    }
}

int main(){
    int lista[6]={4, 0, 5, 2, -1, 9};
    interval(lista, 1, 8);
    return 0;
}