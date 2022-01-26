'''
modifier: 02
eqtime: 35
'''

def main():
    info("Air Pipette x1")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
    
    
