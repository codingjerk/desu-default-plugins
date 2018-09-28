name = 'Autochmod +x plugin'
description = 'Automaticly adds +x flag for local scripts'

import os
import stat

def match(args):
    file_name = args[0]

    if os.path.exists(file_name):
        # TODO: check windows behaviour
        st = os.stat(file_name).st_mode
        if st & stat.S_IEXEC != 0: return False
        
        os.chmod(file_name, st | stat.S_IEXEC)
        return True

def modify(args):
    return args
