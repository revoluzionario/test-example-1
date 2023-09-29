import sys

sys.path.append("./example")
import example as testTarget

test_cases_coverage = [
    (-1, "poor", "Invalid input!"),
    (0, "none", 0),
    (10, "semi", 10907)
]


def test_calculateCost(test_cases):
    i = 1
    for test_value, test_poverty_level, expected_output in test_cases:
        print("Test case", i, "\nActual output:", testTarget.calculateCost(test_poverty_level, test_value),
              "\nExpected output:", expected_output, "\n", testTarget.calculateCost(test_poverty_level, test_value) == expected_output, "\n")
        i += 1

print("Test case for branch coverage:")
test_calculateCost(test_cases_coverage)
