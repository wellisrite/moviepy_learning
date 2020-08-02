import moviepy.editor as mp
from moviepy.editor import TextClip

dirout = ''
mobile_size = (640, 400)
Font = 'Microsoft-JhengHei-Bold-&-Microsoft-JhengHei-UI-Bold'
texts = []


def main():
    ''' main function '''

    intro_duration = 5
    screensize = (1280, 720)
    first_text_y = screensize[1]/6
    second_text_y = screensize[1]/3

    background = mp.ColorClip(screensize, (255, 255, 255), duration=intro_duration)

    first_text = TextClip("Hello world!", fontsize=50, color='black',
                          method="label", size=mobile_size) \
                              .set_duration(intro_duration) \
                              .set_position(("center", first_text_y))

    second_text = TextClip("Hi there", fontsize=50,
                           color='blue', method="label", size=mobile_size) \
                                .set_duration(intro_duration) \
                                .set_position(('center', second_text_y))


    full_text = mp.CompositeVideoClip(
        [background, first_text, second_text])

    full_text.write_videofile(dirout + 'local.mp4', fps=1)


if __name__ == '__main__':
    main()

