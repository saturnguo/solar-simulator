import ctypes

sollib = ctypes.CDLL('./sol_library.so')

sollib.compute_acceleration.argtypes=(
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
)

sollib.update_position.argtypes=(
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
)

sollib.update_velocity.argtypes=(
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
)

def compute_acceleration(x, y, other_mass, other_x, other_y):
    num_bodies = len(other_x)

    other_mass_c = (ctypes.c_double * num_bodies)(*other_mass)
    other_x_c = (ctypes.c_double * num_bodies)(*other_x)
    other_y_c = (ctypes.c_double * num_bodies)(*other_y)

    ax = ctypes.c_double(0)
    ay = ctypes.c_double(0)

    sollib.compute_acceleration(ctypes.byref(ax), ctypes.byref(ay), x, y, 
                                other_mass_c, other_x_c, 
                                other_y_c, num_bodies)
        
    return ax.value, ay.value

def update_position(x, y, v_x, v_y, timestep):
    x_c = ctypes.c_double(x)
    y_c = ctypes.c_double(y)

    sollib.update_position(ctypes.byref(x_c), ctypes.byref(y_c), v_x, v_y,
                           timestep)
    
    return x_c.value, y_c.value

def update_velocity(v_x, v_y, ax, ay, timestep):
    v_xc = ctypes.c_double(v_x)
    v_yc = ctypes.c_double(v_y)

    sollib.update_velocity(ctypes.byref(v_xc), ctypes.byref(v_yc), ax, ay,
                           timestep)

    return v_xc.value, v_yc.value
