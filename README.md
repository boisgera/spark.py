# Spark

### Sparklines with Python 3

See? Here's a graph of your productivity gains after using spark: ▁▂▃▅▇

## Install

The original [spark](https://github.com/holman/spark),
[by Zach Holman](https://github.com/holman/spark/blob/master/LICENSE.md) 
is a [shell script][bin], 
(to be dropped in a directory that's in your `$PATH`).

This Python port can be installed with :

    $ python setup.py install


## Usage

### Command-line interface

    $ python -m spark 0 30 55 80 33 150
    ▁▂▃▅▂▇


### Python interface

    >>> from spark import spark_print
    >>> spark_print([0, 30, 55, 80, 33, 150])
    ▁▂▃▅▂▇





[bin]:      https://github.com/holman/spark/blob/master/spark
[spark]:     https://github.com/holman/spark
[holman]:   https://twitter.com/holman
