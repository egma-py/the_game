from colors import *

import pygame as pg
import pygame.draw as pgd
import math as m


def arc(screen, color, Rect, start_angle, stop_angle, width=0):
    '''
    This function draws an arc better then pygame does.

    Parameters
    ----------
    screen : Surface
    color : tuple or list
    Rect : tuple or list
    start_angle : int
    stop_angle : int
    width : int, optional
        The default is 0.

    Returns
    -------
    None.

    '''
    start_angle_to_deg = int((start_angle*360)/(2*m.pi))
    stop_angle_to_deg = int((stop_angle*360)/(2*m.pi))
    x = Rect[0][0]
    y = Rect[0][1]
    xr = Rect[1][0]//2
    yr = Rect[1][1]//2
    # If width if more than 4, arc is drawn in circles, else in lines(for quality)
    if width >= 4:    
        while start_angle_to_deg != stop_angle_to_deg:
            # Dividing an arc into pieces
            dx = int(xr*m.cos(2*m.pi*start_angle_to_deg/360))
            dy = -int(yr*m.sin(2*m.pi*start_angle_to_deg/360))
            pgd.circle(screen, color, (x+xr+dx, y+yr+dy), width//2)
            start_angle_to_deg += 1
    else:     
        while start_angle_to_deg != stop_angle_to_deg:
            # Dividing an arc into pieces
            dx0 = int(xr*m.cos(2*m.pi*start_angle_to_deg/360)) 
            dy0 = -int(yr*m.sin(2*m.pi*start_angle_to_deg/360))
            dx = int(xr*m.cos(2*m.pi*start_angle_to_deg/360))
            dy = -int(yr*m.sin(2*m.pi*start_angle_to_deg/360))
            pgd.line(screen, color, (x+xr+dx0, y+yr+dy0), (x+xr+dx, y+yr+dy), width)
            start_angle_to_deg += 1
            
            
def roundrect(screen, colors, Rect, width=0, radius=0, R=[-1,-1,-1,-1]): #FIXME add transparence
    '''
    This function draws a rectangle with rounded 
    corners, because pygame doesn't.
    Each rounded corner is drawn with cirlce(width=0)
    If width is not zero, corner is drawn with arc function

    Parameters
    ----------
    screen : Surface
    colors : list
        Contains background and recctangle colors.
    Rect : tuple or list
    width : int, optional
        The default is 0.
    radius : int, optional
        The same for each border radius. The default is 0.
    R : list, optional
        List of each border radius. The default is [-1,-1,-1,-1].

    Returns
    -------
    None.

    '''
    x = Rect[0][0]
    y = Rect[0][1]
    l = Rect[1][0]
    h = Rect[1][1]
    if width%2 != 0:
        width += 1
    if l > h:
        maxR = h//2
    else:
        maxR = l//2
    if radius > maxR:
        radius = maxR
    for i in range(4):
        if R[i] > maxR:
            R[i] = maxR
    # If width if zero, drawing is more simple
    def with_width0():
        if R == [-1, -1, -1, -1]:
            circle_centers = [(x+radius, y+radius),
                              (x+l-radius, y+radius),
                              (x+l-radius, y+h-radius),
                              (x+radius, y+h-radius)]
            pgd.rect(screen, 
                     colors[0], 
                     ((x, y+radius), (l, h-2*radius)), 
                     width)
            pgd.rect(screen, 
                     colors[0],
                     ((x+radius, y), (l-2*radius, h)),
                     width)
            for center in circle_centers:
                if radius != 0:
                    pgd.circle(screen, colors[0], center, radius)
        else:
            circle_centers = [(x+R[0], y+R[0]),
                              (x+l-R[1], y+R[1]),
                              (x+l-R[2], y+h-R[2]),
                              (x+R[3], y+h-R[3])]
            pgd.rect(screen, colors[0], Rect, width)
            pgd.rect(screen, colors[1], ((x, y), (R[0], R[0])), width)
            pgd.rect(screen, colors[1], ((x+l-R[1], y), (R[1], R[1])), width)
            pgd.rect(screen, colors[1], ((x+l-R[2], y+h-R[2]), (R[2], R[2])), width)
            pgd.rect(screen, colors[1], ((x, y+h-R[3]), (R[3], R[3])), width)
            for i in range(4):
                if R[i] <= 0:
                    pass
                else:
                    pgd.circle(screen, colors[0], circle_centers[i], R[i])
    def with_widthnot0():
        if R == [-1, -1, -1, -1]:
            starts = [(x+radius, y), 
                      (x+l, y+radius),
                      (x+l-radius, y+h),
                      (x, y+h-radius)]
            ends = [(x+l-radius, y),
                    (x+l, y+h-radius),
                    (x+radius, y+h),
                    (x, y+radius)]
            circle_rects = [((x, y), (2*radius, 2*radius)),
                            ((x+l-2*radius, y), (2*radius, 2*radius)),
                            ((x+l-2*radius, y+h-2*radius), (2*radius, 2*radius)),
                            ((x, y+h-2*radius), (2*radius, 2*radius))]
            angles = [(m.pi/2, m.pi),
                      (0, m.pi/2),
                      (-m.pi/2, 0),
                      (m.pi, 3*m.pi/2)]
            for i in range(4):
                pgd.line(screen, colors[0], starts[i], ends[i], width)
                start = angles[i][0]
                stop = angles[i][1]
                arc(screen, colors[0], circle_rects[i], start, stop, width)
        else:
            starts = [(x+R[0], y), 
                      (x+l, y+R[1]),
                      (x+l-R[2], y+h),
                      (x, y+h-R[3])]
            ends = [(x+l-R[1], y),
                    (x+l, y+h-R[2]),
                    (x+R[3], y+h),
                    (x, y+R[0])]
            circle_rects = [((x, y), (2*R[0], 2*R[0])),
                            ((x+l-2*R[1], y), (2*R[1], 2*R[1])),
                            ((x+l-2*R[2], y+h-2*R[2]), (2*R[2], 2*R[2])),
                            ((x, y+h-2*R[3]), (2*R[3], 2*R[3]))]
            angles = [(m.pi/2, m.pi),
                      (0, m.pi/2),
                      (-m.pi/2, 0),
                      (m.pi, 3*m.pi/2)]
            for i in range(4):
                pgd.line(screen, colors[0], starts[i], ends[i], width)
                start = angles[i][0]
                stop = angles[i][1]
                arc(screen, colors[0], circle_rects[i], start, stop, width)
    if width == 0:
        with_width0()
    else:
        with_widthnot0()
        
        
def pie(screen, color, Rect, start_angle, stop_angle):
    if start_angle%360 == 0:
        start_angle -= 1
    if stop_angle%360 == 0:
        stop_angle -= 1
    a0 = (2*m.pi)*((start_angle%360)/360)
    a1 = (2*m.pi)*((stop_angle%360)/360)
    if start_angle == stop_angle:
        pgd.ellipse(screen, color, Rect)
    else:
        x_radius = Rect[1][0]//2
        y_radius = Rect[1][1]//2
        center_x = Rect[0][0] + x_radius
        center_y = Rect[0][1] + y_radius
        vertexes = [(center_x+x_radius*m.cos(a0), center_y-y_radius*m.sin(a0)),
                    (center_x, center_y),
                    (center_x+x_radius*m.cos(a1), center_y-y_radius*m.sin(a1))]
        delta = m.pi/20
        while a1-delta >= a0:
            a1 -= delta 
            vertexes.append((center_x+x_radius*m.cos(a1), center_y-y_radius*m.sin(a1)))
        pgd.polygon(screen, color, vertexes)