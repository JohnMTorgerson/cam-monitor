from configure_logging import logger
import libcamera
from picamera2 import Picamera2, Preview
from pprint import pprint

def main() :
    # tuning = Picamera2.load_tuning_file("imx477.json")
    # pprint(tuning)

    # algo = Picamera2.find_tuning_algo(tuning, "rpi.agc")
    # algo["exposure_modes"]["extra_long"] = {
    #     'gain': [1.0,
    #              2.0,
    #              4.0,
    #              6.0,
    #              12.0,
    #              16.0],
    #     'shutter': [100,
    #                 10000,
    #                 30000,
    #                 60000,
    #                 120000,
    #                 240000]
    #     }

    tuning = Picamera2.load_tuning_file("imx477.json")
    algo = Picamera2.find_tuning_algo(tuning, "rpi.agc")
    # pprint(algo)
    algo["channels"][0]["exposure_modes"]["normal"] = {"shutter": [100, 10000, 30000, 70000], "gain": [1.0, 2.0, 4.0, 200.0]}
    # pprint(algo)

    cam = Picamera2(tuning=tuning)
    cam.start_preview(Preview.QTGL)

    # preview_config = cam.create_preview_configuration()
    # preview_config.main.size = (1280,720)
    # cam.configure(preview_config)
    # cam.align_configuration(preview_config)
    # pprint(preview_config)


    # cam.preview_configuration.main.size = (1280,720)
    cam.preview_configuration.main.size = (1920,1044)
    cam.preview_configuration.transform = libcamera.Transform(hflip=True, vflip=True)
    cam.preview_configuration.controls.NoiseReductionMode = 1
    cam.preview_configuration.controls.FrameDurationLimits = (100,66666)
    # cam.preview_configuration.controls.FrameRate = 30

    cam.preview_configuration.controls.AeEnable = True
    cam.preview_configuration.controls.AwbEnable = True
    cam.preview_configuration.align()
    cam.configure("preview")

    cam.title_fields = ["ExposureTime", "AnalogueGain", "DigitalGain"]

    pprint(cam.camera_controls)
    pprint(cam.preview_configuration)

    cam.start()
    message = input("Press enter to quit\n\n") # Run until someone presses enter


if __name__ == "__main__":
    main()
