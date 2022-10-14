import pytest
import os.path

from project import verifyArgv, formatToAscii, generateVideo


def main():
    test_verifyArgv()
    test_formatToAscii()
    test_generateVideo()

def test_verifyArgv():
    # no arguments
    with pytest.raises(SystemExit) as error:
        verifyArgv(["project.py"])
    assert error.type == SystemExit
    assert error.value.code == 1

    # more than 2 arguments
    with pytest.raises(SystemExit) as error:
        verifyArgv(["project.py", "video", "mp4"])
    assert error.type == SystemExit
    assert error.value.code == 1

    # empty filename
    with pytest.raises(SystemExit) as error:
        verifyArgv(["project.py", ""])
    assert error.type == SystemExit
    assert error.value.code == 1

    # invalid filename
    with pytest.raises(SystemExit) as error:
        verifyArgv(["project.py", "video/"])
    assert error.type == SystemExit
    assert error.value.code == 1

    # correct usage
    assert verifyArgv(["project.py", "video"]) == "video"

    
def test_formatToAscii():
    # ASCII characters at the beggining
    assert formatToAscii("abcd|ÿü日本人中國的’∞") == "abcd|ÿü"
    # ASCII characters at the end
    assert formatToAscii("日本人中國的’∞abcd|ÿü") == "abcd|ÿü"
    # ASCII characters at the middle
    assert formatToAscii("日本人中abcd|ÿü國的’∞") == "abcd|ÿü"

def test_generateVideo():
    # generate video(correct)
    generateVideo("cs50", "test_filename", imagesAmount=1, imageDuration=1, width=1920, height=1080, sound=False)
    assert os.path.isfile("test_filename.mp4")

    os.remove("test_filename.mp4")

    # generate video(incorrect)
    generateVideo("cs50", "test_filename2", imagesAmount=1, imageDuration=1, width=1920, height=1080, sound=False)
    assert not os.path.isfile("test_wrong_filename.mp4")

    os.remove("test_filename2.mp4")


if __name__ == "__main__":
    main()