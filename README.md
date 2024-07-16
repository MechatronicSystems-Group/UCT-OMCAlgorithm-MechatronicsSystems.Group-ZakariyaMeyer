# OpticalMotionCapture-ZakariyaMeyer-MechatronicSystems.Group
 Optical motion capture algorithm. 
 
Some files are used for algorithm testing, the main motion capture algorithm is located in 'Motion Capture (final) Code', file name 'MotionCapture.mlx'.

File descriptions are as follows:

Asynch vs Synch SIM TEST:
Used to test the synchronous and asynchronous EKF algorithms in a simulated environment. Feel free to adjust the speed of the simulated rigid-body robot. Code is quite messy and was cleaned up a little in the final code file.

CAM MOUNT DRAWINGS:
The designed gimballed mount drawings are in this file, will still need to add in a few dimensioned drawings for recreation.

EKF-MathValidation:
First iteration of EKF simulation testing to validate the mathematics of the BFT and SFT algorithms. This can be used to recreate the algorithms from scratch. The (gigantic) EKF matrices (such as the observation matrix, system dynamics matrix) are also derived in this file so feel free to take a look. This could also be used to port the algorithm to another coding language as it fully derives the EKF from scratch, using intrinsic and extrinsic parameters generated from first principles rather than using MATLAB functions.

Epipolar Geometry:
This was the simulated and real-world test of correspondence matching using epipolar geometry. In the final code this was scrapped because it slowed down the refresh rate of the EKF. Could be applied to SFT algorithm so that it can estimate the position of multiple features with respect to the inertial frame. 

GUI: 
This is the non-updated GUI, created in the early stages of my dissertation. The GUI was fully discussed in Appendix of the dissertation, and a lot of the features will need to be updated.  

MATLAB INTRINSIC PARAMS:
This is the intrinsic parameters of the specific OpenMV H7 R2 cameras used in my dissertation. The code connects to this file path when setting the intrinsics in the final motion capture code, therefore you might need to edit the final code so that it captures your camera intrinsics rather than these. If you're using the exact same cameras I was using, you still may need to recalibrate them as the focus might have been adjusted :(. This file is just here for completness sake, so feel free to ignore it (or delete it!).

MISC: 
This is misc files, might add a bit more to it but for now it just has a real-world triangulation test. This test was used to verify the accuracy of the calibration process and to see how accurate the cameras were using varying resolutions. This was also developed using first principles!

MotionCapture (final) Code
This is the final code of the optical motion capture algorithm! This was what calculated all the experimental results found in Chapter 5 of my dissertation. This algorithm works quite well and should be used as a baseline if the need to update the GUI ever arises. The format of this algorithm should also be maintained if porting to another programming language. A lot of the code is quite messy so feel free to contact me if there's something you don't understand. The algorithm can also probably be optimized further, but it worked well during my tests.

OpenMV Camera:
This is the MicroPython code for the OpenMV cameras used. Unfortunately it will only work on OpenMV cameras, however you might be able to adjust the code to a different language for other cameras. If doing this, please try to carefully maintain the functionality of this code. There are a lot of instances where the cameras communicate with the base station (.mlx file) and therefore it is basically intertwined with the final MotionCapture.mlx code! The cameras also have their own relevant ID's and this is set as a interger named 'CAMID = ??' for now. Please change this to ID your cameras accordingly!

Recorded Results:
This is the recorded results of the experimental testing, there's about 10 recorded results saved here, however I most likely tested the algorithm over 100 times!!! The results are separated into 3 folder, CamerCountData, EKFData, EncoderData. The camera count data kept track of which camera sent data in each iteration of the EKF. The EKFData is the a posteriori state vector of the EKF in each iteration accompanied by a timestamp of the base stations clock, a refresh rate of the EKF, and the elapsed time of the EKF. The EncoderData is the angular position of the encoder which the platform was attached, accompanied by a timestamp of the base stations clock. All the data is then filtered into a file (located in this folder) called 'MatlabEncoderXEKFResultsComparetor.mlx' which is used to compare the data between the EKF and the Encoder! Feel free to check out the results, and make sure to change the filepath located in the first line of 'MatlabEncoderXEKFResultsComparetor.mlx' file.

README.md:
Hey that's me! Anyway I'll try adding comments to the code so that it's easier to interpret as it does get quite complicated at times. There are some comments at the moment (used to keep me sane whilst developing this) but I'm not too sure if a 'new' user will understand them completely. Again, feel free to contact me if needed!

