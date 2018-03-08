pytl
====
[![0.2.4](https://img.shields.io/badge/pypi-0.2.4-brightgreen.svg)](https://pypi.python.org/pypi/pytl/)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/ryo-ma/pytl/blob/master/LICENSE)

## Overview

Command line tool that parses python file, enumerates classes and methods as a tree structure.


## Usage

``` bash
$ pytl test.py

 2: class Test
 3:   |_def __init__(self)
 6:   |_def walk(self, distance)
 9:   |_def stop(self)
12: def method1()
13:   |_def method2()
14:     |_def method3()
15:       |_def method4()
18: def main()

```

Show only the def line

``` bash
$ pytl test.py -d

 3: def __init__(self)
 6: def walk(self, distance)
 9: def stop(self)
12: def method1()
13:   |_def method2()
14:     |_def method3()
15:       |_def method4()
18: def main()

```

Show only the class line

``` bash
$ pytl test.py -c

 2: class Test

```


## Install

``` bash
$ pip install pytl
```

## Licence

[MIT](https://github.com/ryo-ma/pytl/blob/master/LICENSE)


