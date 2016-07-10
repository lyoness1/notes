"""Lazy Evaluation"""

# Lazy evaluation is a method to avoid throwing errors, by first checking 
# existence before calling on something that isn't there. 

# Ex: 

# would throw error if 'Katie' key wasn't in friends dictionary:
if friends['Katie'].is_free_friday():
    invite_to_party(friends['Katie'])

# Lazy evaluation prevents this key error:
if 'Katie' in friends and friends['Katie'].is_free_friday():
    invite_to_party(friends['Katie'])


# Generator elements in Python are lazy. They don't use space, they just
# generate the next needed item. xrange() and yield are examples. 

for i in xrange(10):
    print "I ate ", i, " cupcakes."

# the list of numbers 1-10 is never created in memory, which saves space. 
# (note: in Python 3, range() is a generator object, so no need for xrange())


# There are lazy and eager design ideas, too. 
# How about keeping track of a maximum? Do it every time you find a max (which
# uses space and time), or just find it when you need it. 

class TemperatureTrackerEager:

    recorded_temperatures = []
    max_temp = None

    def record_temperature(self, temp):
        """Records temperature, checks if max"""
        recorded_temperatures.append(temp)
        if temp > max_temp:
            max_temp = temp


class TemperatureTrackerLazy:

    recorded_temperatures = []

    def record_temperature(self, temp):
        """Records temperature"""
        recorded_temperatures.append(temp)

    def get_max_temp(self):
        """Finds maximum temperature"""
        return max(recorded_temperatures)

# Which is better? It depends on when you want to use the time/space to get max!