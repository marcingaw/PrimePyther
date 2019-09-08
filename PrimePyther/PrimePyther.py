from datetime import datetime

import math

found_primes = [1, 2]
current_value = 3

# print("      1 : 1")
# print("      2 : 2")

while True:
    current_value_sqrt = math.sqrt(current_value)
    found_divider = False
    
    for divider in found_primes[1:]:

        if divider > current_value_sqrt:
            break

        if current_value % divider == 0:
            found_divider = True
            break

        divider = divider + 1

    if not found_divider:
        # print(f"{len(found_primes):7} : {current_value}")
        found_primes.append(current_value)

        if len(found_primes) % 1000 == 0:
            print(f"{len(found_primes):7} @ {datetime.now()} : {current_value}")

        if len(found_primes) >= 1000000:
            break

    current_value = current_value + 1
