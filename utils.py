import cv2

def check_valid(arg, lower_limit, upper_limit, msg):
    if not lower_limit <= arg <= upper_limit:
        print(f"Argumento \'{msg}\' invalido ({lower_limit}-{upper_limit})!")
        exit()
    
    return arg

def invert_range(channel, lower, upper, sign=1):
    mask = cv2.inRange(channel, lower, upper)
    channel[mask > 0] = channel[mask > 0] + sign * 90

    return channel
