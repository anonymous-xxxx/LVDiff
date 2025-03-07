import cv2
import ffmpeg

def change_video_fps(input_video_path, output_video_path, target_fps=16):
    # 打开原始视频文件
    cap = cv2.VideoCapture(input_video_path)
    
    # 获取视频的原始帧率、宽度和高度
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 设置视频写入器，新的输出视频文件
    fourcc = cv2.VideoWriter_fourcc(*'H264')  # 可以根据需要选择不同的编码器  一定要用H264格式
    out = cv2.VideoWriter(output_video_path, fourcc, target_fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 写入每一帧到输出视频文件
        out.write(frame)

    # 释放资源
    cap.release()
    out.release()

    print(f"视频已保存为 {output_video_path}，帧率为 {target_fps} FPS。")


# 使用示例
input_video = r"C:\Users\73977\Desktop\AAAI\LVDiff-page-github\cogvideox_final\FISH_frames241.mp4"
output_video = r"C:\Users\73977\Desktop\AAAI\LVDiff-page-github\cogvideox_final\FISH_frames241_fps8.mp4"
change_video_fps(input_video, output_video, target_fps=8)
