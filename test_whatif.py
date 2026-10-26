
from whatif import simulate_savings


# Test 1: Normal savings calculation
new_units, new_bill, savings = simulate_savings(520, 10, 7)

assert new_units == 468
assert new_bill == 3276
assert savings == 364

print("Normal savings calculation: PASS")


# Test 2: Zero percent reduction
new_units, new_bill, savings = simulate_savings(520, 0, 7)

assert new_units == 520
assert new_bill == 3640
assert savings == 0

print("Zero reduction test: PASS")


# Test 3: Invalid reduction percentage
try:
    simulate_savings(520, 110, 7)
    print("Invalid reduction test: FAIL")

except ValueError:
    print("Invalid reduction test: PASS")


# Test 4: Invalid baseline
try:
    simulate_savings(0, 10, 7)
    print("Invalid baseline test: FAIL")

except ValueError:
    print("Invalid baseline test: PASS")

