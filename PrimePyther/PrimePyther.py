from datetime import datetime

found_primes = [1, 2]
current_value = 3
last_tstamp = datetime.now()

# print("      1 : 1")
# print("      2 : 2")

while True:
    found_divider = False
    
    for divider in found_primes[1:]:

        if divider * divider > current_value:
            break

        if current_value % divider == 0:
            found_divider = True
            break

    if not found_divider:
        # print(f"{len(found_primes):7} : {current_value}")
        found_primes.append(current_value)

        if len(found_primes) % 10000 == 0:
            now_tstamp = datetime.now()
            print(f"{len(found_primes):7} @ {now_tstamp} : {current_value:8} took {now_tstamp - last_tstamp}")
            last_tstamp = now_tstamp

        if len(found_primes) >= 1000000:
            break

    current_value = current_value + 2
