import math
import utils

G = 6.674e-11  # GRAVITATIONAL_CONSTANT
C = 299792458  # SPEED_OF_LIGHT, m/s
SPEED_OF_SOUND = 340.29   # m/s
LUMINOSITY_OF_SUN = 3.8e33


def orbital_period(radius, m):
	return (2 * math.pi) * ( math.pow( ( math.pow(radius, 3) / (G * m) ), 0.5) )


def magnitude_of_acceleration_due_to_surface_gravity(radius, source_mass):
	return (G * source_mass) / (math.pow(radius, 2))

def magnitude_of_acceleration_due_to_rotation(rotational_velocity, radius):
	return math.pow(rotational_velocity, 2) / radius


def angular_velocity(period, radius):
	return (2 * math.pi * radius) / period

# def doppler_shift(freq, period, velocity):
# 	v = (2 * math.pi / r) / period
# 	new_freq = freq * (1 + velocity / C)
# 	return new_freq - freq

def doppler_shift(rest_freq, wave_velocity, source_velocity, observer_velocity):
	'''
	Computes doppler shift in Hertz
	'''
	new_freq = (
		(
			( wave_velocity + observer_velocity ) /
			( wave_velocity - source_velocity )
		) *
		rest_freq
	)

	return new_freq - rest_freq
