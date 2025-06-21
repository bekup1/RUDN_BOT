import logging
from logging import getLogger, FileHandler ,StreamHandler , ERROR , INFO , basicConfig , DEBUG



logger = getLogger()

logger = getLogger() #this logger its root loger, other will inheritance from this log 
def setup_logging():
    import os
    FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, 'dataset.log')

    file_handler = FileHandler(log_path, mode='w')
    file_handler.setLevel(DEBUG)

    console = StreamHandler()
    console.setLevel(ERROR)

    basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])


