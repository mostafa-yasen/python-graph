from typing import Optional

class Graph:
  def __init__(self, graph_dict: Optional[dict] = None) -> None:
    self.dict = graph_dict or {}

  def get_vertices(self) -> list:
    return list(self.dict.keys())

  def find_edges(self):
    edges = []
    for vertix in self.dict:
      for next_vertix in self.dict[vertix]:
        if {next_vertix, vertix} not in edges:
          edges.append({next_vertix, vertix})

    return edges


def main():
  graph_elements = { 
    "a": ["b","c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
  }
  g = Graph(graph_elements)
  print(g.find_edges())

if __name__ == "__main__":
  main()
