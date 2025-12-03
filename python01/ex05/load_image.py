import numpy as np
import PIL.Image
import matplotlib.pyplot as plt
import pimp_image


def ft_load(path: np.array) -> np.array:
    '''Load an image print it's shape, RGB content,
       pimp it with the selected filter name
       and display it'''
    try:
        img = np.asarray(PIL.Image.open(path))
    except Exception:
        print("Error: ft_load arg is not a file or a valid one")
        return

    print(f"The shape of this image is : {img.shape}")
    print(img)

    plt.imshow(img)
    plt.show()
    return (img)


def main():
    img = ft_load("../animal.jpeg")
    pimp_image.ft_invert(img)
    pimp_image.ft_red(img)
    pimp_image.ft_green(img)
    pimp_image.ft_blue(img)
    pimp_image.ft_grey(img)


if (__name__ == "__main__"):
    main()
