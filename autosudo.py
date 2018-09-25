name = 'Autosudo plugin'
description = 'Automaticly runs program with sudo if needed'

def match(args):
    cmd_name = args[0] if len(args) else None
    cmd_args = [arg for arg in args if arg.find('-') == 0]

    if cmd_name == 'pacman':
        for arg in cmd_args:
            # TODO: S and s can be in separated arguments
            if ('S' in arg and 's' not in arg) or ('R' in arg):
                return True
        
    return False

def modify(args):
    return ['sudo'] + args

