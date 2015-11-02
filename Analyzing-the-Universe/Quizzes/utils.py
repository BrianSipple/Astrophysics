import math

SPEED_OF_LIGHT = 299792458  # m / s
KILOMETERS_IN_PARSEC = 3.1e13
AUS_IN_PARSEC = 206265
SECONDS_PER_YEAR = 60 * 60 * 24 * 365
GRAVITATIONAL_CONSTANT = 6.674e-11  # N * m^2/kg^2



def degrees_to_radians(degrees):
    return (degrees / 180) * math.pi

def radians_to_degrees(radians):
    return (radians * 180) / math.pi

def degrees_to_arcseconds(degrees):
    return (degrees % 360) * 3600

def radians_to_arcseconds(radians):
    return degrees_to_arcseconds(radians_to_degrees(radians))

def angular_size(distance_in_arcseconds, object_width_in_arcseconds):
    return radians_to_arcseconds(
        math.asin(object_width_in_arcseconds / distance_in_arcseconds)
    )


def angular_velocity(period, radius):
	return (2 * math.pi * radius) / period




def meters_to_nanometers(meters):
    return math.pow(10, 9) * meters

def kilometers_to_nanometers(kilometers):
    return kilometers * 1e6

def nanometers_to_meters(nanometers):
    return nanometers * 1e-9

def nanometers_to_kilometers(nanometers):
    return nanometers * 1e-6


def joules_to_electron_volts(joules):
    return joules * 6.242e18


def wavelength(freq):
    return SPEED_OF_LIGHT / freq

def frequency(wavelength):
    return SPEED_OF_LIGHT / wavelength


def flux(luminosity, distance):
	return luminosity / (4 * math.pi * math.pow(distance, 2))

def surface_area_of_a_sphere(radius):
    return 4 * math.pi * math.pow(radius, 2)

def luminosity(flux, radius, distance):
    return flux * surface_area_of_a_sphere(distance + (radius / 2) )

def kilometers_to_parsecs(kms):
    return kms / KILOMETERS_IN_PARSEC

def angular_size(object_diameter_in_arcseconds):
    return object_diameter_in_arcseconds / AUS_IN_PARSEC


def distance_to_object(object_diameter, angular_size):
    '''
    Compute distance to an object given its size in diameter,
    and the anguler size in arcseconds
    '''
    return (object_diameter * AUS_IN_PARSEC) / angular_size


def light_years_to_kilometers(light_years):
    return SPEED_OF_LIGHT * 1e-3 * SECONDS_PER_YEAR * light_years


def schwarzchild_radius(black_hole_mass):
    return (
        (2 * GRAVITATIONAL_CONSTANT * black_hole_mass)
        /
        math.pow(SPEED_OF_LIGHT, 2)
    )

def expected_wavelength_shift_from_redshift(redshift, wavelength_at_rest_in_nm):
    return redshift * wavelength_at_rest_in_nm
