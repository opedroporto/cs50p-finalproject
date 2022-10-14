import sys

from video import Video


def main():
    verifyArgv(sys.argv)
    videoName = sys.argv[1]

    print("Welcome to Video Generator!\nPlease tell us your video preferences.")
    
    # word input
    word = input("Video theme: ")
    while not word:
        print("Invalid input. Please, try again.")
        word = input("Video theme: ")
    word = formatToAscii(word)

    # numeric inputs
    imagesAmount = int(input("Images amount (default/recommended: 15): "))
    imageDuration = int(input("Image Duration in sec (default/recommended: 3): "))
    width = int(input("Width in px (default/recommended: 1920): "))
    height = int(input("Height in px (default/recommended: 1080): "))

    # sound input
    sound = input("Audio active? (y(yes)/n(no)): ")
    if sound.lower() in ["y", "yes"]:
        sound = True
    elif sound.lower() in ["n", "no"]:
        sound = False
    else:
        sound = False

    # generate video
    video = generateVideo(word, videoName, imagesAmount, imageDuration, width, height, sound)

    # play video
    video.playVideo()

def verifyArgv(argv):
    # short argv length
    if len(argv) < 2:
        print("Please provide a file name for your video. Usage: python3 project.py [filename]")
        sys.exit(1)
    # long argv length
    if len(argv) > 2:
        print("Please provide only one argument. Usage: python3 project.py [filename]")
        sys.exit(1)

    filename = str(argv[1])
    # filename must not be empty
    if not filename:
        print("The filename must not be empty")
        sys.exit(1)
    # filename must not contain "/""
    if "/" in filename:
        print("The filename must not contain \"/\" (slash character)")
        sys.exit(1)
    
    return formatToAscii(filename)

def formatToAscii(string):
    new_string = ""
    for character in string:
        if ord(character) < 256:
            new_string += character
            
    return new_string

def generateVideo(word, videoName, imagesAmount=15, imageDuration=3, width=1920, height=1080, sound=True):
    video = Video(word, videoName, imagesAmount, imageDuration, width, height, sound)
    print("\n'''\n" + str(video) + "\n'''\n")
    video.generate()

    return video


if __name__ == "__main__":
    main()