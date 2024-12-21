#include <cmath>
#include "sol_library.h"

const double G = 6.67384e-11;

extern "C" {

     void compute_acceleration(double* ax, double* ay, double x, double y, 
                                double* other_mass, double* other_x, 
                                double* other_y, int num_bodies) {

        for (int i = 0; i < num_bodies; ++i) {
            double x_distance = other_x[i] - x;
            double y_distance = other_y[i] - y;
            double distance = sqrt(x_distance * x_distance + y_distance * y_distance);

            double a = G * (other_mass[i] / (distance * distance));

            *ax += a * (x_distance / distance);
            *ay += a * (y_distance / distance);
        }
        
                        }

    void update_position(double* x, double* y, double v_x, 
                        double v_y, double timestep) {

        *x += v_x * timestep;
        *y += v_y * timestep;

                        }

    void update_velocity(double* v_x, double* v_y, double ax,
                        double ay, double timestep) {

        *v_x += ax * timestep;
        *v_y += ay * timestep;

                        }

}