import pytest
from data.particles import Particle, Smoke

def test_particle_update():
    particle = Particle([])

    particle.position = (10, 10)
    particle.change_x = 5
    particle.change_y = 5

    particle.update()

    assert particle.position == (15, 15)

def test_smoke_update():
    smoke = Smoke(10)

    smoke.position = (10, 10)
    smoke.change_x = 5
    smoke.change_y = 5
    smoke.alpha = 255

    orig_scale = smoke.scale

    smoke.update()
    
    assert smoke.position == (15, 15)
    assert smoke.alpha < 255
    assert smoke.scale > orig_scale

# pytest.main(["-v", "--tb=no", "test_particles.py"])