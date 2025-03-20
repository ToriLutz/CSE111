##Victoria lutz 
import math 

def water_column_height (tower_height, tank_height):
    column_height = tower_height + ((3 * tank_height)/4)
    return column_height

def pressure_gain_from_water_height(height):
    p =  998.2 # Density of water in kg/m^3
    g = 9.80665 #Acceleration due to earth's gravity
    pressure = p * g * height / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    p = 998.2 #density of water
    pressure_loss = -friction_factor * pipe_length * p * fluid_velocity**2 /(2000*pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
        p = 998.2 #density of water
        pressure = -0.04 * p * fluid_velocity**2 * quantity_fittings / 2000
        return pressure