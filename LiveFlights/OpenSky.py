from opensky_api import OpenSkyApi

api = OpenSkyApi()
states = api.get_states()

for state_vector in states.states:
    if(39 < state_vector.latitude < 42 and -75 < state_vector.longitude < -70):
        print state_vector.callsign  + "(" + str(state_vector.latitude) + "," + str(state_vector.longitude) + ")" + \
              " alt: " + str(state_vector.geo_altitude) + " , heading: " + str(state_vector.heading)