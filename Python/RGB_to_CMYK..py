# Python code to convert RGB of a color to CMYK.

# Declarying and initializing global variables
RGB_SCALE = 255
CMYK_SCALE = 100

# Declaring function to convert RGB to CMYK
def RGB_to_CMYK(r, g, b):

    print("RGB = ",r,g,b)

    if (r, g, b) == (0, 0, 0):
        print(0, 0, 0, CMYK_SCALE)

    else:
        c = 1 - r / RGB_SCALE
        m = 1 - g / RGB_SCALE
        y = 1 - b / RGB_SCALE

        min_cmy = min(c, m, y)

        c = ((c - min_cmy) / (1 - min_cmy)) * CMYK_SCALE

        m = ((m - min_cmy) / (1 - min_cmy)) * CMYK_SCALE

        y = ((y - min_cmy) / (1 - min_cmy)) * CMYK_SCALE

        k = min_cmy

    print("CMYK = ", round(c), round(m), round(y), round(k))

# Initializing/Calling the declared function
RGB_to_CMYK(15, 240, 254)
