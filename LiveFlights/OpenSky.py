from opensky_api import OpenSkyApi

api = OpenSkyApi()
states = api.get_states()

for state_vector in states.states:
    print state_vector.callsign