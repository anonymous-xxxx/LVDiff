import cv2

# 打开视频文件
keep_frames = 161
video_path = r'C:\Users\73977\Desktop\AAAI\LVDiff-page-github\videos\long_examples\1000_frames_a pair of dancing lovers in the center.mp4'  # 替换为你的视频路径
output_path = r'C:\Users\73977\Desktop\AAAI\LVDiff-page-github\videos\good_wan\t2v-1.3B_832_480_1_1_A_balloon_filled_with_water_was_thrown.mp4'  # 新视频保存路径

cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 获取视频的帧率、宽度和高度
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定义视频编码器（例如：MP4V）
fourcc = cv2.VideoWriter_fourcc(*'H264')  # 可以根据需要更改编码器

# 创建 VideoWriter 对象，用于保存新视频
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 初始化帧计数器
frame_count = 0

# 循环读取视频帧
while True:
    # 读取一帧
    ret, frame = cap.read()

    # 如果读取失败（例如视频结束），退出循环
    if not ret:
        break

    # 保存前100帧到新视频
    if frame_count < keep_frames:
        out.write(frame)  # 将帧写入新视频
        frame_count += 1
    else:
        break

# 释放资源
cap.release()
out.release()

print(f"Finished saving frames to {output_path}.")