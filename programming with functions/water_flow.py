##Victoria lutz 
##For extra credit I made a function that makes pascal to psi 


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
    
def reynolds_number(hydraulic_diameter, fluid_velocity):
        p = 998.2 #density of water
        u = 0.0010016 
        reynolds = p * hydraulic_diameter * fluid_velocity / u
        return reynolds
    
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    r = reynolds_number
    p = 998.2 #density of water
    k = (0.1 + (50/r)) * ((larger_diameter/smaller_diameter)**4 - 1)
    pressure = (-k)* p * fluid_velocity**2/2000
    return pressure 
##EXTRA CREDIT changing kpa to psi and testing it as well as printing 
def kpa_to_psi (pressure):
    psi = pressure * 0.145038
    return psi
    
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
     ##Calculating kpa to PSI 
    pressure_in_psi = kpa_to_psi (pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_in_psi:.1f} PSI")
    
if __name__ == "__main__":
    main()