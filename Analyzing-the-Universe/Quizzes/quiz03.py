import math

SECONDS_PER_DAY = 60 * 60 * 24

# meters per second
VELOCITY_FROM_EARTH_ROTATION = (2 * math.pi * 6e6) / SECONDS_PER_DAY

# meters per second squared
MAX_CENTRIPEDAL_ACCELERATION_FROM_EARTH_ROTATION = math.pow(VELOCITY_FROM_EARTH_ROTATION, 2) / 6e6
