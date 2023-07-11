import sys


def prints(content) -> None:
    """
    Allows the text on the terminal to be overwritten so that updates appear on a single line, rather than underneath.

    :returns: None
    """
    sys.stdout.write('\r')
    sys.stdout.write(content)
    sys.stdout.flush()
