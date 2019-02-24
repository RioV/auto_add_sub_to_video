from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips


def sub_config(txt):
    text_clip = TextClip(txt, font='Helvetica Neue', fontsize=40, color='white')
    text_clip = text_clip.on_color(size=(int(text_clip.w * 1.05), int(text_clip.h * 1.05)), col_opacity=0.5)
    return text_clip

# generator = lambda txt: TextClip(txt, font='Helvetica Neue', fontsize=40, color='white').on_color(col_opacity=0.5)

subtitles = SubtitlesClip("The Power of Chlorophyll.srt", sub_config)
intro_video = VideoFileClip("Intro HanaPhuong 1.mp4")
video = VideoFileClip("The Power of Chlorophyll.mp4")

result = CompositeVideoClip([video, subtitles.set_position(('center', 0.8), relative=True)])
result = concatenate_videoclips([intro_video, result], method='compose')
result.write_videofile("The Power of Chlorophyll-yt.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


# srt file : add thêm 1 line ở đít
# file nếu ko phải mp4 thì convert về mp
# file nào size bé hơn thì concatenate_videoclips theo file đấy
