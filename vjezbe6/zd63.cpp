#include <iostream>
#include <list>

void interval(int list[], int size, int a, int b){
    for(int i=0; i<size; i++){
        if (list[i] >= a && list[i] <= b){
            std::cout << list[i] << " " ;
        }
    }
}

void replace(int list[], int size, int p1, int p2){
    int a=list[p1];
    int b=list[p2];
    list[p1]=b;
    list[p2]=a;
    }

void reverse(int list[], int size){
    for(int i=0; i<size; i++){
        replace(list, size, i, size-i);
    }
    for(int i=0; i<size; i++){
        std::cout << list[i] << " " ;
}}

int main(){
    int lista[6]={4, 0, 5, 2, -1, 9};
    //interval(lista, 6, 1, 8);
    //replace(lista, 6, 1, 4);
    reverse(lista, 6);
    return 0;
}