import matplotlib.pyplot as plt
import networkx as nx
import os

SCRIPTS_DIR = "./scripts"
TOPO_DIR = "./topo" # topologies folder
FIGSIZE_W = 15  # inch
FIGSIZE_H = 8   # inch
NODE_SIZE = 1000
NODE_COLOR = "red"
EDGE_WIDTH = 0.5
EDGE_COLOR = "black"

os.system(f"{SCRIPTS_DIR}/clear_cache.sh")
logs_file = open("logs", 'w')
plt.rcParams['figure.max_open_warning'] = 0

count = 0
print("Generating graphs...")

for graph_dir in os.listdir(TOPO_DIR):
  graph_dir_path = os.path.join(TOPO_DIR, graph_dir)
  if os.path.isdir(graph_dir_path):
    
    for file in os.listdir(graph_dir_path):
      gml_path = os.path.join(TOPO_DIR, graph_dir, file)
      gml_name = gml_path.split("/")[2]

      try:
        plt.figure(figsize=(FIGSIZE_W, FIGSIZE_H))
        G = nx.read_gml(gml_path)
        nx.draw(G, with_labels=True, edge_color=EDGE_COLOR, node_color=NODE_COLOR, width=EDGE_WIDTH) 
        plt.savefig(f'{graph_dir_path}/{gml_name}_GRAPH.png')
        plt.close()
 
        plt.figure(figsize=(FIGSIZE_W, FIGSIZE_H))
        mst = nx.minimum_spanning_tree(G)
        pos = nx.spring_layout(mst)
        nx.draw(mst, pos, with_labels=True, edge_color=EDGE_COLOR, width=EDGE_WIDTH, node_color=NODE_COLOR, node_size=NODE_SIZE)
        plt.savefig(f'{graph_dir_path}/{gml_name}_MST.png')
        plt.close()
        count+=1

      except: 
        logs_file.write(f"Could not generate MST for {gml_name} topology!\n")
logs_file.close()
os.system("clear")
print(f"{count} topologies have been processed!")
