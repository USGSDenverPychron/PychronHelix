'''
modifier: 01
eqtime: 30
'''

def main():
    info("Air Pipette x3")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    
    #shot 1
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
    sleep(1)
    
    #shots 2-3
    for i in range(2):
        info('Shot {}'.format(i+2))
        gosub('common:FillPipette2')
        gosub('common:ExpandPipette2')
        close(description='Outer Pipette 2')
        sleep(1)
