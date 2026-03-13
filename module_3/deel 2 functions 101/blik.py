import math

def calculate_cilinder_content(diameter, hoogte):
    straal = diameter / 2
    inhoud = math.pi * straal**2 * hoogte
    return round(inhoud, 1)