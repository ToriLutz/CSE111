import pytest 
from pytest import approx
##this is to get the function from water_flow.py
from water_flow import water_column_height

def test_water_column_height():
  assert water_column_height(0,0) == approx(0.0, rel=0.01)
  assert water_column_height(0,10) == approx(7.5, rel = 0.01)
  assert water_column_height(25.0, 0) == approx (25.0, rel = 0.01)
  assert water_column_height(48.3, 12.8) == approx (57.9, rel=0.01)
        
        
##pressure 
from water_flow import pressure_gain_from_water_height

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx (0, abs == 0.001)
    assert pressure_gain_from_water_height(30.2) == approx (295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)
    
from water_flow import pressure_loss_from_pipe
def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx (0.000, abs= 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx (0.000, abs= 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx (0.000, abs= 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx (-113.008, abs= 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx (-100.462, abs= 0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx (-61.576, abs= 0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx (-110.884, abs= 0.001)
    
from water_flow import pressure_loss_from_fittings

def test_pressure_loss_from_fittings():
    pressure_loss_from_fittings(0, 3) == approx (0, abs=0.001)
    pressure_loss_from_fittings(1.65, 0) == approx (0, abs=0.001)
    pressure_loss_from_fittings(1.65, 2) == approx (-0.109, abs=0.001)
    pressure_loss_from_fittings(1.75, 2) == approx (-0.122, abs=0.001)
    pressure_loss_from_fittings(1.75, 5) == approx (-0.306, abs=0.001)