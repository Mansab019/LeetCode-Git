def findHighestAltitude(gain):
    # your code here
    altitude = 0
    max_altitude = 0
    for i in range(len(gain)):
        altitude += gain[i]
        max_altitude = max(max_altitude, altitude)
    return max_altitude

# Test
gain = [-5, 1, 5, 0, -7]
print(findHighestAltitude(gain))  # Expected: 1