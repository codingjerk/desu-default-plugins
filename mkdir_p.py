name = 'Mkdir -p plugin'
description = 'Automaticly adds -p flag to mkdir'

def match(args):
    cmd_name = args[0] if len(args) else None
    return cmd_name == 'mkdir'

def modify(args):
    return args[:1] + ['-p'] + args[1:]
