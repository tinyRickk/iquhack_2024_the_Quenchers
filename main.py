from perceval.components import catalog
from perceval.components import PS, Port
from perceval.utils import Encoding
from numpy import pi
import perceval as pcvl
def get_CCZ() -> pcvl.Processor:
  #creating single qubit T
  t = (pcvl.Circuit(2, name="T")
       .add(1, PS(pi/4))
       )
  #creating Tdg
  tdg = (pcvl.Circuit(2, name="Tdg")
       .add(1, PS(7*pi/4))
       )
  #initializing the processor
  CCZ_processor = pcvl.Processor("CliffordClifford2017", 6)
  #Creating the Toffoli gate
  CCZ_processor = (CCZ_processor
                 .add_port(0, Port(Encoding.DUAL_RAIL, 'ctrl'))
                 .add_port(2, Port(Encoding.DUAL_RAIL, 'ctrl'))
                 .add_port(4, Port(Encoding.DUAL_RAIL, 'data'))
                 .add(2, catalog['heralded cnot'].build_processor())
                 .add(4, tdg)
                 .add((0,1,4,5), catalog['heralded cnot'].build_processor())
                 .add(4, t)
                 .add((2,3,4,5), catalog['heralded cnot'].build_processor())
                 .add(4, tdg)
                 .add((0,1,4,5), catalog['heralded cnot'].build_processor())
                 .add(2, t)
                 .add(4, t)
                 .add(0, catalog['heralded cnot'].build_processor())
                 .add(0, t)
                 .add(2, tdg)
                 .add(0, catalog['postprocessed cnot'].build_processor())
                 )
  
  return CCZ_processor
