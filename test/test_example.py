import sys

sys.path.append("./example")
import example as testTarget

test_cases_partition = [
    (-1, "poor", "Invalid input!"),
    (23, "none", 38594),
    (76, "poor", 64492),
    (128, "semi", 147544.8),
    (240, "semi", 307736),
    (369, "none", 821146),
    (450, "none", 1348050),
    (100, "poor", 85300),
]
test_cases_decision = [
    (-1, "poor", "Invalid input!"),
    (23, "none", 38594),
    (76, "none", 128984),
    (128, "none", 226992),
    (240, "none", 473440),
    (369, "none", 821146),
    (450, "none", 1348050),
    (12, "semi", 13088.4),
    (68, "semi", 74822.8),
    (176, "semi", 210381.6),
    (290, "semi", 390156),
    (400, "semi", 590850),
    (560, "semi", 1085513),
    (34, "poor", 28526),
    (51, "poor", 42817),
    (199, "poor", 184993),
    (203, "poor", 189804),
    (398, "poor", 451666),
    (401, "poor", 602313.5),
]

def test_calculateCost(test_cases):
    i = 1
    for test_value, test_poverty_level, expected_output in test_cases:
        print("Test case", i, "\nActual output:", testTarget.calculateCost(test_poverty_level, test_value),
              "\nExpected output:", expected_output, "\n", testTarget.calculateCost(test_poverty_level, test_value) == expected_output, "\n")
        i += 1

print("Test case for equivalence partition:")
test_calculateCost(test_cases_partition)

print("Test case for decision board:")
test_calculateCost(test_cases_decision)