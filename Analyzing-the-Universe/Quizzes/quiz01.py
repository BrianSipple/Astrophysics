import math
from constants import *
from utils import *
#from ...lib.helpers.unitConversion import *



def magnitude_from_brightness(brightness):

    return brightness / 2.512;


def brightness_difference_factor_from_magnitudes(mag1, mag2):
    mag_diff = mag1 - mag2
    #return pow(2.512, mag_diff)
    return (mag_diff / 5) * 100

'''
If you have a convex lens that has a focal length of 2.55 cm,
and an object that is 20 cm away from it, how far away will the image
appear from the lens in cm? Round your answer to the nearest tenth of a centimeter.
'''
def opposite_distance_through_lens(initial_distance, focal_length):

    # 1 / f = 1 / do + 1 / d1
    return 1 / ( (1 / focal_length) - (1 / initial_distance) )


'''
To get a magnification of 0.2X for any object, you use a convex
lens that has a focal length of 7.5mm. How far must you place the
object from the lens? Round your answer to the nearest mm.
'''
def magnification(dist_image, dist_object):
    return dist_image / dist_object



def seconds_of_light_travel_in_meters(meters):
    return meters / SPEED_OF_LIGHT


def speed_through_medium(wavelength, frequency):
    '''
    Computes speed of a wave through any given medium
    @param wavelength: wavelength in meters
    @param frequency: frequency in Hertz
    '''
    return wavelength * frequency


def photon_energy_from_frequency(frequency):
    return frequency * PLANCKS_CONSTANT


def photon_energy_from_wavelength(wavelength):
    return (SPEED_OF_LIGHT * PLANCKS_CONSTANT) / wavelength


def wavelength_from_joules(joules):
    return (PLANCKS_CONSTANT * SPEED_OF_LIGHT) / joules
