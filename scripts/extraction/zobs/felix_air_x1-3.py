'''
modifier: 02
eqtime: 35
'''

def main():
    info("Air Pipette x1-3")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    
    open('Q')
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    
    gosub('common:ExpandPipette2')
    
    close(name='Q')
    close(description='Outer Pipette 2')
    
    
