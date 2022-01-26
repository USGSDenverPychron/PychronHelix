'''
modifier: 03
eqtime: 25
'''

def main():
    info("Cocktail Pipette x1")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')

    #shot 1
    gosub('common:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette1')
    close(description='Outer Pipette 1')
    sleep(1)
    
    #shots 2-5
    for i in range(4):
        info('Shot {}'.format(i+2))
        gosub('common:FillPipette1')
        gosub('common:ExpandPipette1')
        close(description='Outer Pipette 1')
        sleep(1)
    