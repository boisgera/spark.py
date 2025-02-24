# -*- coding: utf-8 -*-

"""
Spark
================================================================================

A port of @holman's [spark] project for Python 3.

[spark]: https://github.com/holman/spark
"""

import sys

ticks = " ▁▂▃▄▅▆▇█"


def spark_string(ints, fit_min=False):
    """Returns a spark string from given iterable of ints.
    
    Keyword Arguments:
    fit_min: Matches the range of the sparkline to the input integers
             rather than the default of zero. Useful for large numbers with
             relatively small differences between the positions
    """
    min_range = min(ints) if fit_min else 0
    step_range = max(ints) - min_range
    step = (step_range / float(len(ticks) - 1)) or 1
    return "".join(ticks[int(round((i - min_range) / step))] for i in ints)


def spark_print(ints, stream=None, fit_min=False):
    """Prints spark to given stream."""
    if stream is None:
        stream = sys.stdout
    stream.write(spark_string(ints, fit_min=fit_min) + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sparks = [int(arg) for arg in sys.argv[1:]]
        spark_print(sparks)
        print
    else:
        usage = print(
            """Spark: ▁▂▃▅▂▇ in your shell

Usage:
  python -m spark [spaces separated values]

Examples:"""
        )

        print("  $ python -m spark 1 5 22 13 53")

        spark_print([1, 5, 22, 13, 53])

        print("  $ python -m spark 0 30 55 80 33 150")

        spark_print([0, 30, 55, 80, 33, 150])
