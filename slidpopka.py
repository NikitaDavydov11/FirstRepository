from moviepy.editor import *


def createImage():

    from PIL import Image, ImageDraw, ImageFont

    im = Image.new('RGB', (1920, 1080), color=('#f3faf0'))

    font = ImageFont.truetype('C:/Windows/Fonts/CENTURY.TTF', size=200)

    dt = ImageDraw.Draw(im)
    dt.text(
        (40, 40),
        'pavka11244',
        font=font,
        fill=('#12345f')
    )

    im.save('C:/Users/student/Documents/122Б/Nikitka/popka5.jpg')


def createMovie():
    vid1 = ImageClip('popka.jpg').set_duration(1)
    vid2 = ImageClip('popka2.jpg').set_duration(2)
    vid3 = ImageClip('popka3.jpg').set_duration(3)
    vid4 = ImageClip('popka4.jpg').set_duration(4)
    vid5 = ImageClip('popka5.jpg').set_duration(5)

    fc = concatenate_videoclips([vid1, vid2, vid3, vid4, vid5], method='compose')
    fc.write_videofile('function.mp4', fps=24)

createMovie()