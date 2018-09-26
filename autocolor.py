name = 'Autocolor plugin'
description = 'Automaticly runs program with --color=auto key if needed'

def match(args):
    cmd_name = args[0] if len(args) else None

    if cmd_name == 'ls':
        return True
        
    return False

def modify(args):
    return args[:1] + ['--color=auto'] + args[1:]

