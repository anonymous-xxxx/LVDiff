import cv2
import os

def video_to_frames(video_path, output_folder):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_count = 0
    
    while True:
        # 读取下一帧
        ret, frame = cap.read()
        
        # 如果读取失败，退出循环
        if not ret:
            break
        
        # 保存帧为图像文件
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        # 打印进度
        print(f"Saved frame {frame_count}")
        
        frame_count += 1
    
    # 释放视频对象
    cap.release()
    print(f"Finished! Total frames saved: {frame_count}")

# 使用示例
video_path = r"C:\Users\73977\Desktop\AAAI\LVDiff-page-github\videos\long_examples\1000_frames_a pair of dancing lovers in the center.mp4"  # 替换为你的视频路径
output_folder = r"C:\Users\73977\Downloads\123"  # 替换为你想保存图像的文件夹路径
video_to_frames(video_path, output_folder)