import heapq
import numpy as np
import matplotlib.pyplot as plt
import cv2

# map
canvas = np.ones((500, 1200, 3))*np.inf
cv2.rectangle(canvas, (95,0), (180,405), (0,0,255), -1)
cv2.rectangle(canvas, (270,95), (355,500), (0,0,255), -1)
hex = np.array([[515,175],[650,95],[785,175],[785,325],[650,405],[515,325]])
hex = hex.reshape(-1,1,2)
cv2.fillPoly(canvas,[hex], color=(0,0,255))
c_shape = np.array([[895,45],[1105,45],[1105,455],[895,455],[895,370],[1015,370],[1015,130],[895,130]])
c_shape = c_shape.reshape(-1,1,2)
cv2.fillPoly(canvas,[c_shape], color=(0,0,255))

# getting user input
count = 0
# start = (8,8)
# end = (1194,340)
start_x = int(input("Enter start x coord: "))
start_y = int(input("Enter start y coord: "))
goal_x = int(input("Enter goal x coord: "))
goal_y = int(input("Enter goal y coord: "))
start = (start_x,goal_y)
end = (goal_x,goal_y)

# cheking if the node is in obstacle
if canvas[500-start[1], start[0]][2] !=np.inf:
    print("please enter new start value")
if canvas[500-end[1], end[0]][2] !=np.inf:
    print("please enter new end value")
# print([500-end[1],end[0]])
# print(canvas[500-end[1],end[0]][2])

# declaring variables and data structs
current_state = (start, start)
q_open = []
q_closed = []
close_heap_dict = {}
all_node = []
back_track_node = []
heapq.heapify(q_open)
heapq.heappush(q_open, (0, current_state))
# function to move up
def up(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1
    current_node  = (current_node[0],current_node[1]+1)
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state))    
                # print("up")     
    return q_open, canvas
# function to move down
def down(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1
    current_node  = (current_node[0],current_node[1]-1)
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state)) 
                # print("down")
    return q_open, canvas
# function to move left
def left(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1
    current_node  = (current_node[0]-1,current_node[1])
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state)) 
                # print("left")
    return q_open, canvas
# function to move right
def right(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1
    current_node  = (current_node[0]+1,current_node[1])
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state)) 
                # print("right")
    return q_open, canvas
# function to up_left 
def up_left(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1.4
    current_node  = (current_node[0]-1,current_node[1]+1)
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state))
                # print("up_left") 
    return q_open, canvas
# function to move up_right
def up_right(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1.4
    current_node  = (current_node[0]+1,current_node[1]+1)
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state)) 
                # print("up_right")
    return q_open, canvas
# function to move down_left
def down_left(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1.4
    current_node  = (current_node[0]-1,current_node[1]-1)
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state)) 
                # print("down_left")
    return q_open, canvas
# function to move down_right
def down_right(q_closed, q_open, canvas, close_heap_dict):
    open_heap_dict = {pair[1][0]: index for index, pair in enumerate(q_open)}
    current_cost = q_closed[-1][0]
    current_node = q_closed[-1][1][0]
    current_parrent = q_closed[-1][1][1]
    parent = current_node
    current_cost+=1.4
    current_node  = (current_node[0]+1,current_node[1]-1)
    current_state = (current_node, parent)
    if (canvas[500-current_node[1],current_node[0]][2] != 255 and 
        5 < current_node[0] < 1195 and
        5 < 500 - current_node[1] < 495):
        if current_node not in close_heap_dict:
            if current_node in open_heap_dict:
                index = open_heap_dict[current_node]
                if q_open[index][0]>current_cost:
                    q_open[index] = (current_cost, current_state)
            else:
                heapq.heappush(q_open, (current_cost, current_state)) 
    return q_open, canvas
# function for back tracking
def back_tracking(q_closed, canvas, count, close_heap_dict):
    if q_closed[-1][1][0] == end:
        node_state = q_closed[-1]
        node = node_state[1][0]
        canvas[500-node[1],node[0]] = (255,0,0)
        while node != start:
            # print(node)
            count+=1
            index = close_heap_dict[node]
            node_state = q_closed[index]
            node = node_state[1][1]
            back_track_node.append(node)
        (print("bt_finished"))
        return canvas
# function to visualize
def visualize(canvas, count, current_Node, back_track_node, all_node, vis_i, vis_j):
    canvas_i = canvas.astype(np.uint8)
    back_track_node.reverse()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('path_visualization.mp4', fourcc, 20.0, (1200, 500))
    for i in all_node:
        cv2.circle(canvas_i, (i[0],500-i[1]), 0, (255,0,0))
        vis_i+=1
        if vis_i%1000 == 0:
            out.write(canvas_i)
        # out.release()
    for j in back_track_node:
        cv2.circle(canvas_i, (j[0],500-j[1]), 0, (255,255,0))
        vis_j+=1
        if vis_j%10 == 0:
            out.write(canvas_i)
    for i in range(50):
        out.write(canvas_i)
    cv2.circle(canvas, (end[0],500-end[1]), 4, (255,255,0), -1)
    cv2.circle(canvas, (start[0],500-start[1]), 4, (255,255,0), -1)
    out.release()
    # cv2.imshow('canva', canvas_i)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()

# while loop for itteration
dict_i = 0
vis_i = 0
vis_j = 0
while True:
    count+=1
    current = heapq.heappop(q_open)
    current_Cost = current[0]
    current_Node = current[1][0]
    # print(current_Node)
    if len(q_open) != 0 or count == 1:# checking the open list lenght
        q_closed.append(current)
        close_heap_dict[current_Node] = dict_i
        dict_i+=1
        if current_Node == end:# checking for the goal node
            print("solution found")
            canvas = back_tracking(q_closed, canvas, count, close_heap_dict)
            visualize(canvas, count, current_Node, back_track_node, all_node, vis_i, vis_j)
            break
        else:
            q_open, _ = up(q_closed, q_open, canvas, close_heap_dict)
            # print(q_open)
            q_open, _ = down(q_closed, q_open, canvas, close_heap_dict)
            q_open, _ = left(q_closed, q_open, canvas, close_heap_dict)
            q_open, _ = right(q_closed, q_open, canvas, close_heap_dict)
            q_open, _ = up_left(q_closed, q_open, canvas, close_heap_dict)
            q_open, _ = up_right(q_closed, q_open, canvas, close_heap_dict)
            q_open, _ = down_left(q_closed, q_open, canvas, close_heap_dict)
            q_open, _ = down_right(q_closed, q_open, canvas, close_heap_dict)
            # print(q_open)
            all_node.append(current_Node)
    else:
        print("No solution found")
        break
# Close any open windows
cv2.destroyAllWindows()