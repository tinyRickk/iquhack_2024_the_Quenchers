#This is an example of the file you must have in your main git branch
import perceval as pcvl

def get_CCZ() -> pcvl.Processor:
    return pcvl.catalog["postprocessed ccz"].build_processor()
