SECONDS_PER_YEAR = 60 * 60 * 24 * 365
SPEED_OF_LIGHT = 299792458  # m / s
KILOMETERS_IN_MEGA_PARSEC = 3.1e19
SPEED_OF_LIGHT_CM = 3e10
HUBBLE_CONSTANT = 71 # km/sec/Mpc

import math

def nanometers_to_meters(nanometers):
    return nanometers * 1e-9

def age_of_the_universe_from_hubble_constant(H):
	'''
	Computes a hypothetical age of the universe if we
	are given a Hubble constant, H, in (km/sec) / Mpc
	'''
	# convert km per second to Mpc per year
	mega_parsecs_per_year = ( H * SECONDS_PER_YEAR ) / KILOMETERS_IN_MEGA_PARSECS

	return 1 / mega_parsecs_per_year


def cluster_recession_speed(distance_in_parsecs):
	mega_parsecs = distance_in_parsecs * 1e-6
	return mega_parsecs * HUBBLE_CONSTANT


def wavelength_shift_from_lab_spectrum(
		scale,
		lab_spectrum_position,
		raw_spectrum_position
	):
	return (raw_spectrum_position - lab_spectrum_position) * scale


def nanometers_per_millimeter_scale(point_1_nm, point_2_nm, point_distance_mm):
	return math.fabs(point_1_nm - point_2_nm) / point_distance_mm


def velocity_of_galaxy_from_nananometer_wavelength_shift(shift, original_wavelength):
	return nanometers_to_meters(shift / original_wavelength) / SPEED_OF_LIGHT  # meters per second


def energy_from_accretion(mass_of_accretion):
	return mass_of_accretion * math.pow(SPEED_OF_LIGHT_CM, 2) * 0.1

def accretion_mass_needed_for_luminosity(luminosity):
	return luminosity / (0.1 * math.pow(SPEED_OF_LIGHT_CM, 2))
