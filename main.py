from configure_logging import logger
try:
    from picamera import PiCamera
except ModuleNotFoundError as e:
    logger.warning(repr(e))
from pynput import keyboard
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

capture_path = os.environ["CAPTURE_PATH"] # the path at which to store static image captures from the stream
try:
    #use sensor_mode=5 to get full field of view (at reduced resolution of 1296x730)
    # https://picamera.readthedocs.io/en/latest/fov.html#sensor-modes
    cam = PiCamera(resolution=(1920, 1080), framerate=30,sensor_mode=5)
    cam.meter_mode = "matrix"
    logger.debug(f"cam.meter_mode == {cam.meter_mode}")
    logger.debug(f"PiCamera.METER_MODES: {PiCamera.METER_MODES}")
except NameError as e:
    logger.warning(repr(e))


def main():
    try:
        # cam.vflip = False
        cam.start_preview()
    except NameError as e:
        logger.warning(repr(e))

    # Collect keyboard events until released
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()

def capture():
    logger.debug("capturing...")
    try:
        filename = datetime.now().strftime("%Y.%m.%d-%H.%M.%S.%f")[:-3] + ".png"
        filepath = capture_path + filename
        logger.debug(f"filepath: {filepath}")
        cam.capture(filepath)
    except Exception as e:
        logger.debug(repr(e))

def change_meter_mode(increment):
    keys = list(PiCamera.METER_MODES)
    logger.debug(f"keys: {keys}")
    i = (keys.index(cam.meter_mode)+increment)%len(keys)
    key = keys[i]
    cam.meter_mode = key
    logger.debug(f"cam.meter_mode == {cam.meter_mode}")

def incr_meter_mode():
    change_meter_mode(1)

def decr_meter_mode():
    change_meter_mode(-1)

def stop():
    raise SystemExit

def on_key_press(key):
    try:
        logger.debug(f'alphanumeric key {key.char} pressed (type: {type(key.char)})')
        if key.char == 'q':
            stop()
    except AttributeError as e:
        logger.debug(f'non-alphanumeric key {key} pressed (type: {type(key)}')
        if key == key.enter :
            capture()
        elif key == key.space :
            stop()
        # elif key == key.down :
        #     incr_meter_mode()
        # elif key == key.up :
        #     decr_meter_mode()

def on_key_release(key):
    pass
    # try:
    #     logger.debug(f'alphanumeric key {key.char} pressed')
    # except AttributeError:
    #     logger.debug(f'alphanumeric key {key} pressed')

if __name__ == "__main__":
    main()

