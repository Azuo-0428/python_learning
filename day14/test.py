import module1
import module2

module1.foo()
module2.foo()

import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

from module1 import foo
foo()
from module2 import foo
foo()

from module1 import foo
from module2 import foo
foo()

from module1 import foo as f1
from module2 import foo as f2
f1()
f2()