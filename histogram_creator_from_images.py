"""
This code allows to extract and save histogram plots of all images in a (gray) image library.
"""

from os import listdir
from os.path import isfile, join, dirname, realpath
import cv2
from matplotlib import pyplot as plt


def histogram_creating_from_images():
    """Main Function"""
    image_list = get_image_names()
    print(image_list)
    for img in image_list:
        print("Process has been started...")
        print("Image name: ", img)
        get_histogram(image_name=img, format="png")
        print("Printed!")

    print("Histogram process finished!")


def get_histogram(image_name, format):
    """
    The name and format is the function that gives the histogram of the received picture.
    """

    img_name = "images/" + image_name + "." + format
    gray_img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('Image',gray_img)
    cv2.calcHist([gray_img], [0], None, [256], [0, 256])

    plt.hist(gray_img.ravel(), 256, [0, 256])
    plt.title("Histogram for gray scale picture")
    plt.savefig("histograms/" + image_name + "_hist.jpg")
    # plt.show()


def get_image_names():
    """
    It is a function that gives a list of the picture names in
    the workspace location where the code is running.
    """
    file_path = get_current_workspace()
    image_list = read_image_list(file_path)
    return image_list


def get_current_workspace():
    """
    It is the function that gives the workspace location where the Tool works.
    """
    file_path = dirname(realpath(__file__))
    return file_path


def read_image_list(file_path):
    """
    Image list reader
    """
    onlyfiles = [
        f
        for f in listdir(file_path + "/images")
        if isfile(join(file_path + "/images", f))
    ]
    image_list = [i.split(".", 1)[0] for i in onlyfiles]
    return image_list


"""
def image_show():

    gray_img = cv2.imread('images/sp_5.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Image',gray_img)

    while True:
        k = cv2.waitKey(0) & 0xFF     
        if k == 27: break             # ESC key to exit
    cv2.destroyAllWindows()
"""
histogram_creating_from_images()
