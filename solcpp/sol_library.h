// sol_library.h

#ifndef sol_library_h
#define sol_library_h

#ifdef __cplusplus
extern "C" {
#endif

void compute_acceleration(double* ax, double* ay, double x, double y, 
                            double* other_mass, double* other_x, double* other_y,
                            int num_bodies);

void update_position(double* x, double* y, double v_x, 
                    double v_y, double timestep);

void update_velocity(double* v_x, double* v_y, double ax,
                        double ay, double timestep);

#ifdef __cplusplus
}
#endif

#endif
