import math

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




def meters_to_nanometers(meters):
    return math.pow(10, 9) * meters


def joules_to_electron_volts(joules):
    return joules * 6.242e18
