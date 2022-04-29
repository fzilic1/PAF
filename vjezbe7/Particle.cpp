#include <Particle.h>
#include <math.h>

using namespace std;

#define PI 3.14159265

Particle::Particle(double v, double theta, double x0, double y0, double step){
    t=0;
    vx=v*cos(theta*PI/180.0);
    vy=v*sin(theta*PI/180.0);
    x=x0;
    y=y0;
    dt=step;
}

Particle::~Particle(){
   
}

void Particle::move(){
    t+=dt;
    x+=vx*dt;
    y+=vy*dt;
    vy+=g*dt;
}

double Particle::range(){
    move();
    while(y > 0){
        move();
    };
    return(x);
}

double Particle::time(){
    move();
    while(y > 0){
        move();
    };
    return(t);
}