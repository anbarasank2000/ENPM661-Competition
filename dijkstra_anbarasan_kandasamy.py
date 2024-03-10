import heapq
import numpy as np
import matplotlib.pyplot as plt
import cv2
# output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can use other codecs like 'MJPG' or 'H264'
fps = 25.0  # Frames per second
width, height = 640, 480  # Video resolution
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))
# map
canvas = np.ones((500, 1200, 3))*np.inf
# c2c_map = np.ones((500, 1200, 1))*np.inf
cv2.rectangle(canvas, (95,0), (180,405), (0,0,255), -1)
# cv2.rectangle(c2c_map, (95,0), (180,405), (-1), -1)
cv2.rectangle(canvas, (270,95), (355,500), (0,0,255), -1)
# cv2.rectangle(c2c_map, (280,105), (355,500), (-1), -1)
hex = np.array([[515,175],[650,95],[785,175],[785,325],[650,405],[515,325]])
hex = hex.reshape(-1,1,2)
cv2.fillPoly(canvas,[hex], color=(0,0,255))
# cv2.fillPoly(c2c_map,[hex], color=(-1))
c_shape = np.array([[895,45],[1105,45],[1105,455],[895,455],[895,370],[1015,370],[1015,130],[895,130]])
c_shape = c_shape.reshape(-1,1,2)
cv2.fillPoly(canvas,[c_shape], color=(0,0,255))
# cv2.fillPoly(c2c_map,[c_shape], color=(-1))