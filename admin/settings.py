env = 'nas'

if env == 'raspberry':
    from .settings_raspberry import *
elif env == 'server':
    from .settings_server import *
elif env == 'nas':
    from .settings_nas import *
else:
    from .settings_local import *

from .settings_secret import *
