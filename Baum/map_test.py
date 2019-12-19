#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import gps_map_marker
import webbrowser
import folium

server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"
mssql = main(server, user, password, database)

tag_id = 'id00001'
i = query_table_id(tag_id)
gps_map_marker(i)

# gpss = []
# for baum in i:
#     print(baum)
#     g = baum['GPS']
#     gps = eval('[' + g + ']')
#     print(gps)
#     gpss.append(gps)
#     if gpss[0] == gpss[-1]:
#         m = folium.Map(location=gpss[0], zoom_start=16)
#     info = baum['tag_id'] + ' ' + baum['date']
#     print(info)
#     folium.Marker(gps, popup=info).add_to(m)
#
# ls = folium.PolyLine(locations=gpss, color='blue', opacity='0.3')
# ls.add_to(m)
# m.save('temp.html')
# webbrowser.open("temp.html")



