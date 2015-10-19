import math

SPEED_OF_LIGHT = 299792458  # m / s


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
