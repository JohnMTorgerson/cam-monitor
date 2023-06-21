from configure_logging import logger
from picamera2 import Picamera2, Preview
from pprint import pprint

def main() :
    cam = Picamera2()
    pprint(cam.camera_controls)
    cam.start_preview(Preview.QTGL)

    preview_config = cam.create_preview_configuration()
    cam.configure(preview_config)

    cam.start()
    message = input("Press enter to quit\n\n") # Run until someone presses enter


if __name__ == "__main__":
    main()
