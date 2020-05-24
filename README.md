## Image segmentation based on Colour Masking



The prerequisite of this method is obviously that the relevant object should be differently colored than the background of the image. A typical example of this is extraction of foliage from background dirt for plant identification.<br/>
For more information go to this article:<br/>
 <Github File Link> <https://github.com/teamHexMtech/IRS-RS-2019-04-27-IS01PT-GRP-Hex-ISS_CHATBOT/tree/master/UserGuide>
 
 <br/>
 <br/>
 The Target Image is first converted to HSV image:<br/>
 
 
 ![HSV Image](https://github.com/RamdasKrishnakumar/Color-Segmentation/blob/master/output%20Images/hsv1.png)
 <br/>
 The HSV image is then thesholded and is further masked to create the segmented image:<br/>
 
 ![Segmented Image](https://github.com/RamdasKrishnakumar/Color-Segmentation/blob/master/output%20Images/green1.png)
<br/>
<br/>
The data for the project can be found here:
https://vision.eng.au.dk/plant-seedlings-dataset/
