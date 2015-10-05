import math
import constants



def standard_deviation(values):

    if len(values) < 2:
        raise ValueError('Standard deviation needs at least two values to be computed')

    mean = sum(values) / len(values)
    sum_of_squared_errors = 0

    #print('Mean: {}'.format(mean))

    for i in range(len(values)):
        squared_error = math.pow( (values[i] - mean), 2 )
        #print('Squared error of {}: {}'.format(values[i], squared_error))
        sum_of_squared_errors += squared_error

    # Square root of average squared error (with average being sum over n-1)
    return math.pow(
        ( 1 / (len(values) - 1) ) * sum_of_squared_errors,
        0.5
    )


def expected_parallax_at_light_years(light_years):
    '''
    Returns the expected parralax, in arcseconds, of a stellar object that
    is a given distance in light years away
    '''
    parsecs = (light_years / 3.3)   # 3.3 LIGHT_YEARS_IN_PARSEC

    return 1 / parsecs


def wavelength_of_hydrogen_electron_level_jump(initial_level, final_level):

    r = 1.0974e7  # Rydberg Constant, meters

    
