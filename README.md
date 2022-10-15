# Video Generator
## Video Demo:  https://youtu.be/X5WWWlwqJMo
[![Video Demo](https://img.youtube.com/vi/X5WWWlwqJMo/maxresdefault.jpg)](https://youtu.be/X5WWWlwqJMo)

## Overall Description:
**<br>&nbsp;&nbsp;&nbsp;&nbsp;This Python application is a video generator. When initialized you are prompted for, among other video specifications, the video theme.<br>&nbsp;&nbsp;&nbsp;&nbsp;Based on the chosen theme, the application, underneath the hood, download images about it and a non-copyrighted song from the Internet. All images and the song are merged together in a mp4 video. As result, the produced video is saved in the “root” (i.e., top-level folder) of the project with the specified name. Basically, you pick a theme and get a video!**

## Project:
The **video.py** file contains the **Video class**, which has the following methods:<br>
 - **__init__**: It is the constructor method of **Video**. It, besides of initializing some constants, sets the following properties:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_word: the video theme;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_videoName: the video file name;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_imagesAmount: the amount of different images about that theme to be searched;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_imageDuration: the duration amount that each image appears on the video given in seconds;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_width: the video resolution width given in pixels;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_height: the video resolution height given in pixels;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_sound: a bool variable that defines if the video must or must not have audio.<br>
 - **__str__**: it returns a string containing the video specifications.<br>
- **__initSeleniumDriver**: it mostly initiates the Selenium (open-source tool that automates web browsers) driver.<br>
- **__retrieveImages**: by using the **Selenium** driver headlessly (which means this has no visual effect as the browser will not show up to the application user), it scrapes the "google.com" for images about the given theme<br>
- **__retrieveSong**: by using the **Selenium** driver, it downloads a non-copyrighted song from the Internet.<br>
- **__writeVideo**: here is where moviepy comes into action. With all the images and the song, a mp4 video is produced by using the **moviepy** library.<br>
- **__deleteTemporaryFiles**: it deletes all temporary files generated throughout the process such as the downloaded images and the song.<br>
- **__quitSeleniumDriver**: it quits the **Selenium** driver, terminating the webdriver window.<br>
- **generate**: it puts all the methods together in a way the required video is produced.<br>
- **playVideo**: it plays the generated video.<br>
 
The **project.py** file is responsible for the main logic and it contains the following functions:<br>
 - **main()**: handles prompting the user for the following video specifications:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;word;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;imagesAmount;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;imageDuration;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sound.<br>
once it has all these informations, it generates a **video** object with the **generateVideo()** function; and finally, the **playVideo()** method of the video is called.

 - **verifyArgv()**: it is called at the beggining of **main()**. This function receives the **sys.argv** (list of command-line arguments passed to the script) and run a serie of verifications to ensure the user passes only 1 argument to the script, which must be a filename that does not contain "/". It returns the filename (first argument) filtered.
 
 - **formatToAscii()**: it is called when receiving user input in **main()**. This function receives a string and returns the same string filtered, removing every character that is not one of the first 255 ASCII characters.
 
 - **generateVideo()**: as mentioned above, this function is used to create a video, and it does it by receiving the video specifications as arguments, passing these arguments to initiate a object from **Video class**, printing the object as a string and finally calling the method **generate()** of the video object. This function returns the video object itself.

The **test_project.py** file is responsible for testing the 3 functions of "project.py" (verifyArgv, formatToAscii, generateVideo) with the following functions:<br>
 - **test_verifyArgv()**: ensures that **verifyArgv()** verifies correctly the amount of command-line arguments and returns the filename as expected. In other words, make sure the script's usage works just as follows:
![example2](https://user-images.githubusercontent.com/77935889/195926287-01e40023-9251-4fd3-b284-71014b2ac2ab.png)
 - **test_formatToAscii()**: ensures that **formatToAscii()** filters the string based on the first 255 ASCII only independent from where the characters are located in the string.
 - **test_generateVideo()**: ensures that **generateVideo()** in fact creates a mp4 video in the root of the project and ensures the video is created with the specified **videoName** preceded by ".mp4". It is done by generating test videos and excluding them right after.

The **helpers.py** file contains **the resize()** function. This function is used by the Video class to resize the downloaded images to the video resolution; it receives a image (Image object from **PIL** library), a width value and height value. It resizes the image by the given resolution and return the image itself.

## Files walkthrough:
**video.py**: <pre>This file is the application core as it contains the **Video class**, responsible for doing everything underneath the hood; it, for example, stores the video specifications, retrieves the images and the song online, produces the video based on the specifications and open the video itself.<br></pre>

**project.py**: <pre>It is the main file of the application and all of the video functionalities are imported and organized here. It is where the main application logic is implemented, which means it handles prompting the user for the video specifications, handling the input, creating a Video object based on that and calling the required object methods for generating and opening the video.<br></pre>

**test_project.py**: <pre>All test functions are in this file. It contains functions with the same name as the tested functions prepend with "test_". This file is used by the **pytest** module to run unit tests on the project.<br></pre>

**README.md**: <pre>It is this file.<br></pre>

**helpers.py**: <pre>Contains a useful python function that is used in the application.<br></pre>

**requirements.txt**: <pre>All libraries required for running this application are here.<br></pre>


## How to use it?
**Step 1**: Clone this repository.<br>
&nbsp;&nbsp;&nbsp;&nbsp;```git clone [this repository web URL]```<br>
&nbsp;&nbsp;&nbsp;&nbsp;```cd [repository folder]```
<br>

**Step 2**: Once you are into the cloned repository folder, install all the requirements with:<br>
&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install -r requirements.txt```
<br>

**Step 3**: Execute the script with:<br>
&nbsp;&nbsp;&nbsp;&nbsp;```python3 project.py [filename]```
<br>

**Step 4**: Fill out the required informations:<br>
&nbsp;&nbsp;&nbsp;&nbsp;![example](https://user-images.githubusercontent.com/77935889/195925806-507c3fe7-e009-4ccf-b93d-aa50879cdc95.png)
<br>

**Step 5**: And Finally, wait for your video to be generated. As soon as it is ready, your video will be saved and will open as the following example of generated video (but in mp4 extension):<br>
&nbsp;&nbsp;&nbsp;&nbsp;

https://user-images.githubusercontent.com/77935889/195937197-4204d1ac-1fa3-4400-a36e-7b9f118d6f01.mov


## References:
- [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022)
- [CS50P Final Project Instructions](https://cs50.harvard.edu/python/2022/project)
- [CS50’s Introduction to Programming with Python (at EDX)](https://www.edx.org/course/cs50s-introduction-to-programming-with-python)
- [CS50 Youtube Channel](https://www.youtube.com/c/cs50)

