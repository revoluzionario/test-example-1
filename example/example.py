electricity_rates = [
      (1, 50, 1678),
      (51, 100, 1734),
      (101, 200, 2014),
      (201, 300, 2536),
      (301, 400, 2834),
      (301, float("inf"), 2927),
  ]
povertyScales = {"none": 0, "semi": 0.35, "poor": 0.5}

def calculateCost(povertyLevel, units):
    if units < 0:
        return "Invalid input!"
    elif units == 0:
        return 0
    
    cost = 0
    for slab_start, slab_end, rate in electricity_rates:
        if units > slab_end:
            cost += (slab_end - slab_start + 1) * rate
        elif units <= slab_end and units >= slab_start:
            cost += (units - slab_start + 1) * rate
            break

    return cost*(1-povertyScales[povertyLevel])
