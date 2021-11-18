import streamlit as st
from tubemap import tubemap
import time

st.markdown("<h1 style='text-align: center; color: white;'>Delhi Metro Travel Planner</h1>", unsafe_allow_html=True)
st.image('./metro.jpg')
st.markdown("<h2 style='text-align: center; color: white;'>Enter Station Names</h2>", unsafe_allow_html=True)
m1 = st.text_input("Source")
m2 = st.text_input("Destination")


def find_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  for node in graph[start]:
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath: return newpath
  return None

def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths

        
def find_shortest_path(graph, start, end, shortestLength=-1, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  shortest = None
  for node in graph[start]:
    if node not in path:
      if shortestLength==-1 or len(path)<(shortestLength-1):
        newpath = find_shortest_path(graph, node, end, shortestLength, path)
        if newpath:
          if not shortest or len(newpath) < len(shortest):
            shortest = newpath
            shortestLength = len(newpath)  
  return shortest        
        
        
stationFrom=m1
stationTo=m2
if(st.button('Search')):
	st.write("Searching shortest route... This may take a while...")
	path=find_shortest_path(tubemap,stationFrom,stationTo)
	my_bar = st.progress(0)
	for percent_complete in range(100):
			time.sleep(0.001)
			my_bar.progress(percent_complete + 1)

	st.write("Suggested Route: ")
	st.write(path)

