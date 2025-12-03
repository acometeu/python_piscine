import numpy as np
import PIL.Image
import matplotlib.pyplot as plt
from zoom import zoom_animal


def ft_load():
    '''Load an image print it's shape, RGB content
    and display a zoom of it using opencv-python library'''
    try:
        img = np.asarray(PIL.Image.open("../animal.jpeg"))
    except Exception:
        print("Error: ft_load arg is not a file or a valid one")
        return

    print(f"The shape of this image is : {img.shape}")
    print(img)

    img = zoom_animal(img)
    print(f"The new shapeafter slicing : {img.shape}")
    print(img)

    plt.imshow(img)
    plt.show()


def main():
    ft_load()


if (__name__ == "__main__"):
    main()
