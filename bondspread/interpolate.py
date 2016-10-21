def interpolate(low, high, function, point):
    if high==low:
        return function(point)
    vh, vl = function(high), function(low)
    return ( (vh-vl)*point + vl* high - vh*low)/(high-low)
