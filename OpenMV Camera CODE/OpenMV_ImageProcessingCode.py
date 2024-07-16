## Single Color Grayscale Blob Tracking Example
##
## This example shows off single color grayscale tracking using the OpenMV Cam.


import sensor, image, time, math, pyb

# Color Tracking Thresholds (Grayscale Min, Grayscale Max)
# The below grayscale threshold is set to only find extremely bright white areas.

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.
#_______________________
# CAM INTRINSICS ID = ?
camID = '05\n' #ENTER ID NUMBER
#_______________________
# CALIBRATION CODE STEP 1 (RGB):

thresholds = (245, 255)
sensor.reset()
sensor.set_framesize(sensor.VGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
sensor.set_auto_exposure(
    False, exposure_us=int(300)
)
clock = time.clock()
bCalibGRAY = True
bTrack = False
bInt = False
bExt = False
uart = pyb.UART(3,115200)
LEDBlue = pyb.LED(3)
LEDGreen = pyb.LED(2)
LEDRed = pyb.LED(1)

LEDRed.off()
LEDGreen.off()
LEDBlue.on()
#CALIBRATION IN VGA!
while(bCalibGRAY):
    img = sensor.snapshot()
    data = ''
    nDetected = 0
    checkVal = False
    for blob in img.find_blobs([thresholds], pixels_threshold=5, area_threshold=5, merge=True):
        # These values depend on the blob not being circular - otherwise they will be shaky.
        img.draw_rectangle(blob.rect(),[0,0,0])
        img.draw_cross(blob.cx(), blob.cy(),[0,0,0])
        cx = blob.cx()
        cy = blob.cy()
        nDetected = nDetected+1
        data = data + str(cx) + ',' + str(cy) + ','
    if nDetected == 5:
        checkVal = True
    if uart.any():
        uartData_str = uart.readline().decode('utf-8')
        print(uartData_str)
        if uartData_str == 'INT\n':
            LEDRed.on()
            uart.write(camID)
            print(camID)
            bInt = True
        elif uartData_str == 'EXT_GRAY\n':
            LEDGreen.on()
            uart.write(data + '\n')
        elif uartData_str == 'EXT_GRAY_SUCCESS\n':
            bExt = True
            print('RECIEVED')
        elif uartData_str == 'SKIP\n':
            print('SKIPPING CALIBRATION')
            bSkip = True
            break
            bCalibGRAY= False
    if bInt and bExt:
        bCalibGRAY = False
LEDRed.off()
LEDGreen.off()
LEDBlue.off()

time.sleep(2)

LEDRed.on()
LEDGreen.off()
LEDBlue.off()

nSFT = 1
nBFT = 3
nFeatures = 3
bTrack = True
bStart = False
while(bTrack):
    clock.tick()
    img = sensor.snapshot()
    nDetected = 0
    data = ''
    if bStart:
        for blob in img.find_blobs([thresholds], pixels_threshold=5, area_threshold=5, merge=True):
            cx = blob.cx()
            cy = blob.cy()
            nDetected = nDetected+1
            data = data + str(cx) + ',' + str(cy) + ','
            if nDetected == nFeatures:
                break
        timestamp = pyb.millis()-initial_t
        uart.write(str(timestamp) + ':' + data + str(clock.fps())+'\n')
        print(str(timestamp) + ':' + data + str(clock.fps())+'\n')
    if uart.any():
        uartData = uart.readline()
        uartData_str = uartData.decode('utf-8')
        if uartData_str == 'START':
            initial_t = pyb.millis()
            LEDRed.off()
            LEDGreen.on()
            bStart = True
        if uartData_str == 'END':
            bStart = False
            LEDGreen.off()
            LEDRed.on()
        if uartData_str == 'BFT':
            nFeatures = nSFT
            LEDR
        if uartData_str == 'SFT':
            nFeatures = nSFT

