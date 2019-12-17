#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import folium
import webbrowser
m = folium.Map(location=[50.783111, 6.046532],
               zoom_start=16)
tooltip = 'Click me!'   # 鼠标放在图标上就显示信息
# popup 点一下显示信息
folium.Marker([50.783067, 6.045786], popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)
folium.Marker([50.783111, 6.046532], popup='<i>Mt. Hood Meadows</i>').add_to(m)
m.add_child(folium.LatLngPopup()) # 弹出经纬度
# m.add_child(folium.ClickForMarker(popup='Waypoint'))   # 通过点击在地图上标记 标记可以拖动

# 在地图上划线
ls = folium.PolyLine(
    locations=[[50.783067, 6.045786],
               [50.783111, 6.046532]],
                color='blue')
ls.add_to(m)
m.save('1.html')
webbrowser.open("1.html")

