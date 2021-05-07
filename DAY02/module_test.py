from module01 import foo
foo()

from module02 import foo
foo()

import module01 as m1

m1.foo()

import module02 as m2

m2.foo()