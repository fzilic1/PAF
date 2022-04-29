class HarmonicOscillator{

    private:
        double t, x, v, k, m, a;
        double dt;

        void move();

    public:
        HarmonicOscillator(double x0, double v0, double k, double m, double step=0.001);
        ~HarmonicOscillator();

        void oscillate(double x0, double v0, double to);
        double period();

};