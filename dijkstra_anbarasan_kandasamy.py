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
count = 0
# print(canvas)
# plt.imshow(canvas)
# plt.show()
start = (8,8)
end = (8,300)
# cv2.circle(canvas, (end[0],500-end[1]), 4, (255,255,0), -1)
if canvas[500-start[1], start[0]][2] !=np.inf:
    print("please enter new start value")
if canvas[500-end[1], end[0]][2] !=np.inf:
    print("please enter new end value")
print([500-end[1],end[0]])
print(canvas[500-end[1],end[0]][2])
cv2.circle(canvas, (end[0],500-end[1]), 4, (255,255,0), -1)
# cv2.imshow("ss", canvas)
# cv2.waitKey(0)
# print(canvas[160,514][2]==np.inf)

current_state = (start, start)
q_open = []
q_closed = []
heapq.heapify(q_open)
# heapq.heapify(q_closed)
heapq.heappush(q_open, (0, current_state))
# print(q_open[0][1][1])

def up():

def down():

def left():

def right():

def back_tracking():
    
while True:
    count+=1
    current_State = heapq.heappop(q_open)
    current_Node = current_State[1][0]
    # print(current_Node)
    if len(q_open) != 0 or count == 1:
        q_closed.append(current_State)
        close_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_closed)}
        # print(close_heap_dict)
        if current_Node == end:
            print("solution found")
            canvas = back_tracking(q_closed, canvas, count, out, close_heap_dict)
            break
        else:
            up()
            down()
            left()
            right()
    else:
        print("No solution found")
        break
out.release()
# Close any open windows
cv2.destroyAllWindows()