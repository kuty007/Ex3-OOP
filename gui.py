import math

import pygame
import pygame_widgets
from pygame_widgets.button import Button
from numpy import inf
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

pygame.init()
win = pygame.display.set_mode((900, 700))
button = Button(win, 20, 20, 20, 20)
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


run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    # Now
    pygame_widgets.update(events)

    # Instead of
    button.listen(events)
    button.draw()
    drew_graph_nodes(win, "blue", graph, radius)
    drew_edges(win, "black")

    pygame.display.update()
