'''
modifier: 01
eqtime: 30
'''

def main():
    info("Air Pipette x4")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    
    #shot 1
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
    sleep(1)
    
    #shots 2-4
    for i in range(3):
        info('Shot {}'.format(i+2))
        gosub('common:FillPipette2')
        gosub('common:ExpandPipette2')
        close(description='Outer Pipette 2')
        sleep(1)
