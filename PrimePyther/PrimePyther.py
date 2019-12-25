from datetime import datetime

found_primes = [1, 2]
linear_factor_sum = 2.0  # 1/1 + 2/2
current_value = 3
last_tstamp = datetime.now()

while True:
    found_divider = False
    
    for divider in found_primes[1:]:

        if divider * divider > current_value:
            break

        if current_value % divider == 0:
            found_divider = True
            break

    if not found_divider:
        found_primes.append(current_value)
        linear_factor_sum = linear_factor_sum + (current_value / len(found_primes))

        if (len(found_primes) < 20):
            print(f"{len(found_primes):7} : {current_value:8} ; l. factor sum : {linear_factor_sum:10.5f}")

        if len(found_primes) % 10000 == 0:
            now_tstamp = datetime.now()
            print(f"{len(found_primes):7} @ {now_tstamp} : "
                  f"{current_value:8} took {now_tstamp - last_tstamp} ; "
                  f"avg l. factor : {(linear_factor_sum / 10000.0):10.5f}")
            linear_factor_sum = 0.0
            last_tstamp = now_tstamp

        if len(found_primes) >= 1000000:
            break

    current_value = current_value + 2
