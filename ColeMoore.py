def week_1():
    def rect_area(length, width):
        return length * width

    def rect_surface_area(length, width, height):
        lw_area = 2 * rect_area(length, width)
        lh_area = 2 * rect_area(length , height)
        wh_area = 2 * rect_area(width, height)
        return lw_area + lh_area + wh_area

    length = int(input("Enter dimension for length"))
    width = int(input("Enter dimension for width"))
    height = int(input("enter dimension for height"))

    surface_area = rect_surface_area(length, width, height)
    print("Surface area of the rectangular solid with dimensions", length, "by", width, "by", height, "is: ", surface_area,
          "units\u00b2")


week_1()
