def week_1():
    def rect_area(length, width):
        return length * width

    def rect_surface_area(length, width, height):

        front_area = rect_area(length, height)
        side_area = rect_area(width, height)
        top_area = rect_area(length, width)
        return  2 * (front_area + side_area + top_area)

    length = int(input("Enter the length of the object as in integer: "))
    width = int(input("Enter the width of the object as in integer: "))
    height = int(input("Enter the height of the object as in integer: "))

    surface_area = rect_surface_area(length, width, height)

    print("Length = ", length, "Width = ", width, "Height = ", height)
    print("Total surface area = ", surface_area)

week_1()