from PIL import Image
import matplotlib.pyplot as plt
import networkx as nx

def find_path(G, start, end):
    path = nx.dijkstra_path(G, start, end)
    length = nx.dijkstra_path_length(G, start, end)
    return path, length

def draw_path(G, pos, path, image_path="dam_sen_map.png"):
    img = Image.open(image_path)
    width, height = img.size

    plt.figure(figsize=(10, 8))
    plt.imshow(img, extent=[0, width, height, 0], origin="upper")

    # Vẽ graph
    nx.draw(G, pos=pos, with_labels=True, node_color="lightblue", node_size=2000)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

    # Đường đi đỏ
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos=pos, edgelist=path_edges, edge_color="red", width=3)

    plt.title("Đường đi tối ưu trong Công viên Đầm Sen")
    plt.axis("off")
    plt.tight_layout()

    output_path = "result_path.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    return output_path
