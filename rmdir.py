name = 'Rm dir (-r) plugin'
description = 'Automaticly adds -r flag to rm'

def match(args):
    cmd_name = args[0] if len(args) else None
    return cmd_name == 'rm'

def modify(args):
    return args[:1] + ['-r'] + args[1:]
