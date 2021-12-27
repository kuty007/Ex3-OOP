import math
from tkinter import filedialog

import pyautogui as pyautogui
# import pygameMenuPro
import pygame
import pygame_menu
import pygame_widgets
from numpy.distutils.fcompiler import pg
from pygame import surface, mouse
from pygame_widgets.button import Button
from numpy import inf

from GraphAlgo import GraphAlgo
import pygame_gui

graph = GraphAlgo()
graph.load_from_json("A5.json")
radius = 10
win = pygame.display.set_mode((900, 700))


def scale_data():
    gr = graph
    x_min = inf
    x_max = -inf
    y_min = inf
    y_max = -inf
    for i in gr.get_graph().get_all_v():
        loction = gr.get_graph().get_node(i).get_location()
        if loction[0] > x_max:
            x_max = loction[0]
        if loction[0] < x_min:
            x_min = loction[0]
        if loction[1] > y_max:
            y_max = loction[1]
        if loction[1] < y_min:
            y_min = loction[1]

    return x_max, x_min, y_max, y_min


def drew_graph_nodes(win_size, color, gra: GraphAlgo(), radius):
    data = scale_data()
    w, h = pygame.display.get_surface().get_size()
    scale_x = w / abs(data[0] - data[1]) * 0.7
    scale_y = h / abs(data[2] - data[3]) * 0.7
    for i in gra.get_graph().get_all_v():
        loc = gra.get_graph().get_node(i).get_location()
        x = (loc[0] - data[1]) * scale_x * 0.97 + 27
        y = (loc[1] - data[3]) * scale_y * 0.97 + 27
        pygame.draw.circle(win_size, color, (x, y), radius)
        bigfont = pygame.font.SysFont("arial", 18)
        text = bigfont.render(str(i), True, "yellow")
        # put the label object on the screen at point x=100, y=100
        win.blit(text, (x, y))


def drew_edges(win_size, color):
    data = scale_data()
    w, h = pygame.display.get_surface().get_size()
    scale_x = w / abs(data[0] - data[1]) * 0.7
    scale_y = h / abs(data[2] - data[3]) * 0.7
    for i in graph.get_graph().get_all_v():
        for j in graph.get_graph().all_out_edges_of_node(i):
            loc_src = graph.get_graph().get_node(i).get_location()
            loc_dst = graph.get_graph().get_node(j).get_location()
            loc_src_x = (loc_src[0] - data[1]) * scale_x * 0.97 + 27
            loc_src_y = (loc_src[1] - data[3]) * scale_y * 0.97 + 27
            loc_dst_x = (loc_dst[0] - data[1]) * scale_x * 0.97 + 27
            loc_dst_y = (loc_dst[1] - data[3]) * scale_y * 0.97 + 27
            start = (loc_src_x, loc_src_y)
            end = (loc_dst_x, loc_dst_y)
            draw_arrow(win, color, start, end)


def draw_arrow(screen, colour, start, end):
    pygame.draw.line(screen, colour, start, end, 2)
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    pygame.draw.polygon(screen, (200, 0, 0), (
        (end[0] + 6 * math.sin(math.radians(rotation)), end[1] + 6 * math.cos(math.radians(rotation))),
        (end[0] + 6 * math.sin(math.radians(rotation - 120)), end[1] + 6 * math.cos(math.radians(rotation - 120))),
        (end[0] + 6 * math.sin(math.radians(rotation + 120)), end[1] + 6 * math.cos(math.radians(rotation + 120)))))


def draw_center(screen, colour, node_id):
    if node_id < 0:
        return
    else:
        data = scale_data()
        w, h = pygame.display.get_surface().get_size()
        scale_x = w / abs(data[0] - data[1]) * 0.7
        scale_y = h / abs(data[2] - data[3]) * 0.7
        loc = graph.get_graph().get_node(node_id).get_location()
        x = (loc[0] - data[1]) * scale_x * 0.97 + 27
        y = (loc[1] - data[3]) * scale_y * 0.97 + 27
        pygame.draw.circle(screen, colour, (x, y), radius)


def draw_shortest_path(colour, node_list: list):
    if len(node_list) < 1:
        return
    else:
        data = scale_data()
        w, h = pygame.display.get_surface().get_size()
        scale_x = w / abs(data[0] - data[1]) * 0.7
        scale_y = h / abs(data[2] - data[3]) * 0.7
        for i in node_list:
            loc = graph.get_graph().get_node(i).get_location()
            x = (loc[0] - data[1]) * scale_x * 0.97 + 27
            y = (loc[1] - data[3]) * scale_y * 0.97 + 27
            pygame.draw.circle(win, colour, (x, y), radius)
        for i in range(len(node_list) - 1):
            loc_src = graph.get_graph().get_node(node_list[i]).get_location()
            loc_dst = graph.get_graph().get_node(node_list[i + 1]).get_location()
            loc_src_x = (loc_src[0] - data[1]) * scale_x * 0.97 + 27
            loc_src_y = (loc_src[1] - data[3]) * scale_y * 0.97 + 27
            loc_dst_x = (loc_dst[0] - data[1]) * scale_x * 0.97 + 27
            loc_dst_y = (loc_dst[1] - data[3]) * scale_y * 0.97 + 27
            start = (loc_src_x, loc_src_y)
            end = (loc_dst_x, loc_dst_y)
            draw_arrow(win, "blue", start, end)


pygame.init()
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(800, 270, 140, 32)
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive
nodes_id_input = ''
active = False

"""Load/Save"""
button_load = Button(win, 800, 0, 100, 20, text='Load Graph', radius=20, inactiveColour=(127, 0, 255),
                     hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_save = Button(win, 800, 25, 100, 20, text='Save Graph', radius=20, inactiveColour=(127, 0, 255),
                     hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
"""Algo"""
button_tsp = Button(win, 800, 50, 100, 20, text='Find Tsp', radius=20, inactiveColour=(127, 0, 255),
                    hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_center = Button(win, 800, 75, 100, 20, text='Find ceter', radius=20, inactiveColour=(127, 0, 255),
                       hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_shortestPath = Button(win, 800, 100, 100, 20, text='Shortest Path', radius=20, inactiveColour=(127, 0, 255),
                             hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_connected = Button(win, 800, 125, 100, 20, text='Is Connected', radius=20, inactiveColour=(127, 0, 255),
                          hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
"""Graph Basic Actions"""
button_addNode = Button(win, 800, 150, 100, 20, text='Add Node', radius=20, inactiveColour=(127, 0, 255),
                        hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_addEdge = Button(win, 800, 175, 100, 20, text='Add Edge', radius=20, inactiveColour=(127, 0, 255),
                        hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_removeNode = Button(win, 800, 200, 100, 20, text='Remove Node', radius=20, inactiveColour=(127, 0, 255),
                           hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))
button_removeEdge = Button(win, 800, 225, 100, 20, text='Remove Edge', radius=20, inactiveColour=(127, 0, 255),
                           hoverColour=(255, 192, 203), font=pygame.font.SysFont('calibri', 15))

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

        if button_load.clicked:

            filename = filedialog.askopenfilename(title="Open graph from file")
            graph.load_from_json(filename)
            print(filename)
            pyautogui.alert("Graph " + str(filename) + " was loaded")

        if button_save.clicked:
            filepath = filedialog.asksaveasfilename(title="Open graph from file")
            graph.save_to_json(filepath)
            pyautogui.alert("Graph was saved")
            print("saved")
        if button_center.clicked:
            center = graph.centerPoint()

            if center[0] > -1:
                pyautogui.alert(center)
                draw_center(win, (200, 0, 0), center[0])
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(2 * 1000)
            else:
                pyautogui.alert(center)

        if button_tsp.clicked:
            if len(nodes_id_input) > 0:
                test_list = nodes_id_input.split(',')
                test_list = list(map(int, test_list))
                x = graph.TSP(test_list)
                pyautogui.alert(x)
                draw_shortest_path("orange", x[0])
                nodes_id_input = ''
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(2 * 1000)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if event.key == pygame.K_RETURN:
                nodes_id_input = user_text
                user_text = ''
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
        if button_connected.clicked:
            if (graph.is_connect()):
                pyautogui.alert("Graph is connected")
            else:
                pyautogui.alert("Graph isn't connected")

        if button_shortestPath.clicked:
            if len(nodes_id_input) > 0:
                test_list = nodes_id_input.split(',')
                test_list = list(map(int, test_list))
                x = graph.shortest_path(test_list[0], test_list[1])
                pyautogui.alert(x)
                nodes_id_input = ''
                draw_shortest_path("green", x[1])
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(2 * 1000)

        if button_addEdge.clicked:
            if len(nodes_id_input) > 0:
                test_list = nodes_id_input.split(',')
                test_list = list(map(int, test_list))
                graph.get_graph().add_edge(test_list[0], test_list[1],1)


        if button_addNode.clicked:
            x, y = mouse.get_pos()
            graph.get_graph().add_node((graph.get_graph().v_size() + 1), (x, y))




        if button_removeEdge.clicked:
            if len(nodes_id_input) > 0:
                test_list = nodes_id_input.split(',')
                test_list = list(map(int, test_list))
                graph.get_graph().remove_edge(test_list[0], test_list[1])

        if button_removeNode.clicked:
            if len(nodes_id_input) > 0:
                test_list = nodes_id_input.split(',')
                test_list = list(map(int, test_list))
                x = test_list[0]
                graph.get_graph().remove_node(x)

    win.fill((0, 0, 0))
    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(win, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    # render at position stated in arguments
    win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame_widgets.update(events)
    # Instead of
    button_load.listen(events)
    button_save.listen(events)
    button_tsp.listen(events)
    button_center.listen(events)
    button_connected.listen(events)
    button_addNode.listen(events)
    button_addEdge.listen(events)
    button_removeNode.listen(events)
    button_removeEdge.listen(events)
    button_load.draw()
    button_save.draw()
    button_tsp.draw()
    button_center.draw()
    button_connected.draw()
    button_addNode.draw()
    button_addEdge.draw()
    button_removeNode.draw()
    button_removeEdge.draw()
    drew_graph_nodes(win, "blue", graph, radius)
    drew_edges(win, "white")
    pygame.display.update()
