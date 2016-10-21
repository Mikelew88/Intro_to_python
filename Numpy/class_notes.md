# Arrays (Numpy)!

Heres some practice: (https://www.hackerrank.com/domains/python/numpy)

```Python
import numpy as np

import sys

arr = np.array(input(),float)

print arr[::-1]

import numpy as np
import sys

print(np.array(input().split(),int).reshape(3,3)
```

### Random stuff

```Python
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def getAllPrimeFactors(n):
    ans = []
    for i in range(2,n/2):
        if n%i==0:
            if isprime(i):
                ans.append(i)
    return sorted(ans)

```
