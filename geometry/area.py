# Geometry utilities

def area_of_rectangle(width, height):
    return width * height


if __name__ == "__main__":
    w = 4
    h = 5
    area = area_of_rectangle(w, h)
    print(f"Area of {w} x {h} rectangle is {area}")