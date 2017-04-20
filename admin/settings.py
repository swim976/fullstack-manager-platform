env = 'local'

if env == 'raspberry':
    from .settings_raspberry import *
elif env == 'server':
    from .settings_server import *
else:
    from .settings_local import *

from .settings_secret import *
