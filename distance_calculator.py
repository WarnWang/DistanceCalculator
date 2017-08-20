#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Filename: distance_calculator
# @Date: 8/8/2017
# @Author: Mark Wang
# @Email: wangyouan@gamil.com

"""
This file is used to calculate the minimal distance between a point and a state

state name please look state_name.py
"""

import shapefile
from vincenty import vincenty


def calculate_shortest_distance_between_point_state(point_x, point_y, state_name):
    sf = shapefile.Reader('shapefile/cb_2016_us_state_500k/cb_2016_us_state_500k')
    for rec in sf.shapeRecords():
        if rec.record[5] == state_name:
            break

    else:
        raise ValueError('Unknown state name {}. Please refer to state_name.py.'.format(state_name))

    min_dis = float('inf')
    for y, x in rec.shape.points:
        dis = vincenty((point_x, point_y), (x, y), miles=False)
        min_dis = min(dis, min_dis)

    return min_dis


if __name__ == '__main__':
    from state_name import StateName

    print(calculate_shortest_distance_between_point_state(35, -77, StateName.MAINE))
