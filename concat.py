from moviepy.editor import VideoFileClip, concatenate_videoclips

# 读取三段视频
video1 = VideoFileClip(r"C:\Users\73977\Desktop\AAAI\LVDiff-page-github\videos\rebuttal\I2V_48.mp4")
video2 = VideoFileClip(r"C:\Users\73977\Downloads\20250308_122754.mp4")
video3 = VideoFileClip(r"C:\Users\73977\Downloads\20250308_124558.mp4")

# 合并视频
final_video = concatenate_videoclips([video1, video2, video3])

# 输出合成后的完整视频
final_video.write_videofile(r"C:\Users\73977\Downloads\output1.mp4", codec="libx264")
