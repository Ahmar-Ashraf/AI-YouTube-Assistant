from moviepy.editor import VideoFileClip

def create_shorts(input_video, output_video, start_time, end_time):
    video = VideoFileClip(input_video).subclip(start_time, end_time)
    video.write_videofile(output_video, fps=30)

create_shorts("final_video.mp4", "shorts.mp4", 10, 30)
print("Shorts video saved as shorts.mp4")