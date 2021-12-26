import math

import pyautogui as pyautogui
import pygameMenuPro
import pygame
import pygame_menu
import pygame_widgets
from pygame import surface
from pygame_widgets.button import Button
from numpy import inf

import gui
from GraphAlgo import GraphAlgo
import pygame_gui


pygame.init()
win = pygame.display.set_mode((900, 700))


"""Load/Save"""
button_load = Button(win, 800, 0, 100, 20 , text='Load Graph', radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_save = Button(win, 800, 25, 100, 20,  text='Save Graph',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
"""Algo"""
button_tsp = Button(win, 800, 50, 100, 20,  text='Find Tsp',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_center = Button(win, 800, 75, 100, 20,  text='Find ceter',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_shortestPath = Button(win, 800, 100, 100, 20,  text='Shortest Path',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_connected = Button(win, 800, 125, 100, 20,  text='Is Connected',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
"""Graph Basic Actions"""
button_addNode = Button(win, 800, 150, 100, 20,  text='Add Node',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_addEdge = Button(win, 800, 175, 100, 20,  text='Add Edge',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_removeNode = Button(win, 800, 200, 100, 20,  text='Remove Node',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))
button_removeEdge = Button(win, 800, 225, 100, 20,  text='Remove Edge',radius=20,inactiveColour=(127,0,255), hoverColour = (255, 192, 203),font = pygame.font.SysFont('calibri', 15))



graph = GraphAlgo()
graph.load_from_json("A5.json")
radius = 10




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

"""def menu():
    print()"""

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

        if button_load.clicked:
            graph.load_from_json("A4.gson")
            print("Loaded")

        if button_save.clicked:
            graph.save_to_json("A14.gson")
            pyautogui.alert("Graph was saved")

            print("saved")
        if button_center.clicked:
            pyautogui.alert(graph.centerPoint())

        if button_tsp.clicked:
            print("להוסיף ליסט לבדיקה")

        if button_connected.clicked:
            if(graph.is_connect()):
                pyautogui.alert("Graph is connected")
            else:
                pyautogui.alert("Graph isn't connected")

        if button_shortestPath.clicked:
            pyautogui.alert(graph.shortest_path(34,37))
            print(graph.shortest_path(34,37))

        if button_addEdge.clicked:
            print("added")
        if button_addNode.clicked:
            print("added")

        if button_removeEdge.clicked:
            print("removed")

        if button_removeNode.clicked:
            print("removed")


    win.fill((0, 0, 0))

    # Now
    pygame_widgets.update(events)

    # Instead of
    button_load.listen(events)
    button_save.listen(events)
    button_tsp.listen(events)
    button_center.listen(events)
    button_connected.listen(events)
    button_addNode.listen(events)
    button_addEdge.listen(events)
    button_removeNode .listen(events)
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

