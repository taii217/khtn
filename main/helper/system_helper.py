import sys


def debugger_is_active() -> bool: # don't allow run in debug
    """Return if the debugger is currently active"""
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None
