from ip2geotools.databases.noncommercial import DbIpCity
import tkinter as tk
import socket
import re
# imports needed packages


def geolocate(ip):
    geo_search = DbIpCity.get(ip, api_key="free")

    geo_text = f"New IP Address found ({ip})\n"
    geo_text += "-" * 30 + "\n"
    geo_text += f"City: {geo_search.city}\n"
    geo_text += f"State/Region: {geo_search.region}\n"
    geo_text += f"Country: {geo_search.country}\n"
    geo_text += f"LAT: {geo_search.latitude}, LON: {geo_search.longitude}"
    # creates text

    root = tk.Tk()
    root.attributes("-topmost", True)
    root.title('New IP Found')
    T = tk.Text(root, height=6, width=50)
    T.pack()
    T.insert(tk.END, geo_text)
    tk.mainloop()
    # shows text window


f = open("data.txt", "r")
ip_info = f.read()
f.close()
# reads in IP info

try:
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ip_info = ip_info.split("â†’")
    ip_info[0] = pattern.search(ip_info[0])[0]
    ip_info[1] = pattern.search(ip_info[1])[0]
    # gathers host and foreign IP

    if ip_info[0] == socket.gethostbyname(socket.gethostname()):  # determines which IP stored is foreign
        ip = ip_info[1]
    else:
        ip = ip_info[0]

    try:  # gets previously found IPs
        g = open("ipcache.txt", "r")
        used_ips = g.readlines()
        g.close()
    except:
        used_ips = []

    find = True

    for used_ip in used_ips:  # if IP has already been found, it won't be displayed
        if used_ip.rstrip("\n") == ip:
            find = False

    if find:
        geolocate(ip)
        # runs function to find geolocation data for IP

        used_ips.append(ip + "\n")
        # adds IP to cache list

        h = open("ipcache.txt", "w")
        h.writelines(used_ips)
        h.close()
        # adds IP to cache file

        e = open("data.txt", "w")
        e.write("")
        e.close()
        # clears data file    
except:
    pass