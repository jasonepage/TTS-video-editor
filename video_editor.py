from moviepy.editor import *

# Load the two videos
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")

# Cut the audio from one of the videos
video2 = video2.without_audio()

# Create a new video by concatenating the two videos horizontally
result = concatenate_videoclips([video1, video2], method="compose")

# Save the result
result.write_videofile("result.mp4")
