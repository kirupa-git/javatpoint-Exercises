print("Area of Triangle:1/2base * Height")

user_base = int(input("Base: "))
user_height = int(input("Height: "))


def area_triangle(base, height):
    print(f"{int(base / 2 * height)}")


area_triangle(user_base,user_height)
