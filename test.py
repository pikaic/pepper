#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import qi
import os

def main():
    # Create a connection to the robot
    session = qi.Session()
    try:
        session.connect("tcp://192.168.1.141:9559")
    except Exception as e:
        print("Could not connect to the robot: {}".format(e))
        return

    # Load an image
    image_path = os.path.join(os.path.dirname(__file__), "image.jpg")
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
    except Exception as e:
        print("Could not load the image: {}".format(e))
        return

    # Display the image on the tablet

    try:
        tablet_service = session.service("ALTabletService")
        tablet_service.showImage(image_data)
    except Exception as e:
        print("Could not display the image: {}".format(e))
        return

if __name__ == "__main__":
    main()