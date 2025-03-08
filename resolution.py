import os
from moviepy.editor import VideoFileClip

# 定义输入和输出文件夹路径
input_folder = r"C:\Users\73977\Downloads\新建文件夹"  # 替换为你的视频文件夹路径
output_folder = r"C:\Users\73977\Downloads\新建文件夹1"     # 替换为输出文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取文件夹中的所有视频文件
for filename in os.listdir(input_folder):
    if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):  # 可以根据需要修改支持的格式
        video_path = os.path.join(input_folder, filename)
        
        # 加载视频文件
        clip = VideoFileClip(video_path)
        
        # 对视频进行裁剪
        resized_clip = clip.resize(newsize=(720, 480))  # 裁剪为512x320
        
        # 保存剪裁后的视频
        output_path = os.path.join(output_folder, f"{filename}")
        resized_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        
        # 关闭视频剪辑，释放资源
        clip.close()
        resized_clip.close()

print("所有视频已成功剪裁完成！")
