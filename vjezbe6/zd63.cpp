#include <iostream>

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
    int li[size];
    for(int i=0; i<size; i++){
        li[size-i-1]=list[i];}
    for(int i=0; i<size; i++){
        list[i]=li[i];
    }}

void sort(int list[], int size){
    for(int i=0; i<size; i++){
        for(int j=i; j<size; j++){
            if(list[j] < list[i]){
                replace(list, size, i, j);
        }}
    }
}

int main(){
    int lista[7]={4, 0, 5, 2, -1, 9, -3};
    //interval(lista, 7, -1, 8);
    sort(lista, 7);
    reverse(lista, 7);
    for(int i=0; i<7; i++){
        std::cout << lista[i] << " " ;}
    return 0;
}