#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import folium
import webbrowser

# 列表转换成字符串
# a =['50.783667', '6.049786']
# stra = ", ".join(a)
# print(stra)

from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import gps_map_marker
from funktion import gps_verarbeitung
server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"
mssql = main(server, user, password, database)
baums=[
    {'device_id': '11111', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.783667', '6.046786', '23', '2'],
    {'device_id': '22222', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.784667', '6.042786', '23', '2'],
    {'device_id': '3333', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.786667', '6.049786', '23', '2'],
    {'device_id': '4444', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.781667', '6.048786', '23', '2']
    ]

tag_id = 'tagid:28984'
delete_table_id(tag_id)
baum_list = gps_verarbeitung(baums)
insert_table_batch(baum_list)
i = query_table_id(tag_id)

for ii in i:
    print(ii)

gps_map_marker(i)

# baums_neu = baums[0::2]
# lis_gps = baums[1::2]
# for baum, gps1 in zip(baums_neu, lis_gps):
#     str_gps = ", ".join(gps1)
#     baum['GPS']=str_gps
#
# print(baums_neu)
#
# def gps_verarbeitung(baum_list):
#     baum_list_new = baum_list[0::2]
#     baum_gps = baum_list[1::2]
#     for baum, gps1 in zip(baum_list_new, baum_gps):
#         str_gps = ", ".join(gps1)
#         baum['GPS'] = str_gps
#     return baum_list_new





#
# gpss = []
# for baum in baums_neu:
#     g = baum['GPS']
#     g_float = map(float, g)
#     gps = list(g_float)
#     gpss.append(gps)
#     info = baum['tag_id'] + ' ' + baum['date']  # add information
#     if gpss[0] == gpss[-1]:
#         m = folium.Map(location=gpss[0], zoom_start=16)
#     folium.Marker(gps, popup=info).add_to(m)
# ls = folium.PolyLine(locations=gpss, color='blue', opacity='0.5')
# ls.add_to(m)
# m.save('temp.html')
# webbrowser.open("temp.html")