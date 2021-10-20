from xlib import facemeta as lib_fm
from xlib import time as lib_time


class FaceAlignerTrainer:
    def __init__(self, faceset_path):
        #fs = self._fs = lib_fm.Faceset(faceset_path)
        fs = lib_fm.Faceset(faceset_path)
        #fs.close()
        
        with lib_time.timeit():
            for x in fs.iter_UImage():
                x.get_image()
            #fs = lib_fm.Faceset(faceset_path)
            #fs.add_UFaceMark( [ lib_fm.UFaceMark() for _ in range(1000)] )
            
        import code
        code.interact(local=dict(globals(), **locals()))

        
    def run(self):
        ...