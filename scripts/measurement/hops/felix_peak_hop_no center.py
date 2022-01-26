#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 120
  detector: H2
  mass: 39.7642
  settling_time: 15.0
default_fits: nominal
equilibration:
  eqtime: 0.0
  inlet: H
  inlet_delay: 3
  outlet: V
  use_extraction_eqtime: true
multicollect:
  counts: 0
  detector: H2
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H2
  detectors:
  - H1
  integration_time: 1.048576
  isotope: Ar40
peakhop:
  generate_ic_table: false
  hops_name: FelixhopsL2_Ar36
  ncycles: 0
  use_peak_hop: true
'''

ACTIVE_DETECTORS=('H2','H1','AX','L1','L2')
NCYCLES=12

def main():
    info('unknown measurement script')
    
    activate_detectors(*ACTIVE_DETECTORS)
   
    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)
    
    hops=load_hops('hops/{}.txt'.format(mx.peakhop.hops_name))
    define_hops(hops)
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    if mx.equilibration.use_extraction_eqtime:
        eqt = eqtime
    else:
        eqt = mx.equilibration.eqtime
        
    equilibrate(eqtime=eqt, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet, 
                delay=mx.equilibration.inlet_delay)
    set_time_zero(0)
    
    # sniff the gas during equilibration
    sniff(eqt)
    set_fits()
    set_baseline_fits()

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=mx.baseline.settling_time)
                  
    # multicollect on active detectors
    # multicollect(ncounts=MULTICOLLECT_COUNTS, integration_time=1)
   
    peak_hop(ncycles=NCYCLES, hops=hops)
    
    if mx.baseline.after:
        # necessary if peak hopping
        define_detectors('Ar40','H2')
        
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=mx.baseline.settling_time)
    
    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector, isotope=mx.peakcenter.isotope,
                   integration_time=mx.peakcenter.integration_time)
    
    if use_cdd_warming:
       gosub('warm_cdd', argv=(mx.equilibration.outlet,))      
       
    info('finished measure script')