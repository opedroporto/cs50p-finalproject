import urllib.request
import moviepy.editor as mp
import time
import glob
import subprocess
import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytube import YouTube
from PIL import Image

from helpers import resize

class Video:
    def __init__(self, word, videoName, imagesAmount=15, imageDuration=1, width=1920, height=1080, sound=True):
        self._word = word
        self._videoName = videoName
        self._imagesAmount = imagesAmount
        self._imageDuration = imageDuration
        self._width = width
        self._height = height
        self._sound = sound
        
        # CONSTANTS
        self._TEMPORARY_FOLDER_PATH = "temporary_assets/"
        self._SONGS_URL = "https://www.youtube.com/c/NoCopyrightSounds/videos" # NoCopyrightSounds Youtube Page
        self._BROWSER_PATH = "/usr/bin/google-chrome"
        self._BROWSER_DRIVER_PATH = "/home/pedro/Downloads/chromedriver"
        self._OPTIONS = Options()
        self._OPTIONS.binary_location = self._BROWSER_PATH
        self._OPTIONS.add_argument("--headless") #set headless mode
    
    def __str__(self):
        return f"Video specs:\n  Video name: {self.videoName}.mp4\n  Theme: {self.word}\n  Image Amount: {self.imagesAmount}\n  Image duration: {self.imageDuration}\n  Width: {self.width}\n  Height: {self.height}\n  Sound: {self.sound}"

    def __initSeleniumDriver(self):
        # init driver
        self._DRIVER = webdriver.Chrome(options = self._OPTIONS, executable_path = self._BROWSER_DRIVER_PATH)

        # define user agent for urllib
        opener = urllib.request.build_opener()
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        urllib.request.install_opener(opener)

    def __retrieveImages(self):
        self._DRIVER.get("https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=" + self.word)
        searches = self._DRIVER.find_elements_by_class_name('islib')

        i = 0
        self._clips = []
        for search in searches[:self.imagesAmount]: 

            # find image link
            search.click()
            time.sleep(3)
            image_link = self._DRIVER.find_element_by_xpath("html/body/div/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div/div/div[3]/div/a/img").get_attribute("src")

            try:
                # download image
                urllib.request.urlretrieve(image_link, self._TEMPORARY_FOLDER_PATH + self.word + str(i))

                # resize image
                img = Image.open(self._TEMPORARY_FOLDER_PATH + self.word + str(i))
                img = img.resize((self.width, self.height), Image.ANTIALIAS).convert("RGB")
                img.save(self._TEMPORARY_FOLDER_PATH + self.word + str(i) + '.jpg')

                # append to the clip list
                for _ in range(self.imageDuration):
                    self._clips.append(self._TEMPORARY_FOLDER_PATH + self.word + str(i) + '.jpg')
            except:
                pass

            i += 1
    
    def __retrieveSong(self):
        # retrieve SONG
        self._DRIVER.get(self._SONGS_URL)
        song_path = self._DRIVER.find_elements_by_id('thumbnail')[1].get_attribute('href')
        song_url = "https://www.youtube.com" + song_path
        self._song = YouTube(song_url).streams.first().download(self._TEMPORARY_FOLDER_PATH, filename="song.mp3")

    def __writeVideo(self):
        # concatenate VIDEOS
        video = mp.ImageSequenceClip(self._clips, fps = 1)

        if self._sound:
            # set audio
            self._song = mp.AudioFileClip(self._TEMPORARY_FOLDER_PATH + "song.mp3").set_duration(video.duration)
            video = video.set_audio(self._song)

        video.write_videofile(self.videoName + ".mp4", fps = 1)
    
    def __deleteTemporaryFiles(self):
        files = glob.glob(self._TEMPORARY_FOLDER_PATH + "*")
        for file in files:
            os.remove(file)

    def __quitSeleniumDriver(self):
        self._DRIVER.quit()

    def generate(self):
        self.__initSeleniumDriver()
        self.__retrieveImages()
        if self.sound:
            self.__retrieveSong()
        self.__writeVideo()
        self.__deleteTemporaryFiles()
        self.__quitSeleniumDriver()

    def playVideo(self):
        try:
            os.startfile(self.word + ".mp4")
        except:
            try:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, self.videoName + ".mp4"])
            except:
                pass

    @property
    def word(self):
        return self._word
    @property
    def videoName(self):
        return self._videoName
    @property
    def imagesAmount(self):
        return self._imagesAmount
    @property
    def imageDuration(self):
        return self._imageDuration
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def sound(self):
        return self._sound