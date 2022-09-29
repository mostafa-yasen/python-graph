from typing import Optional

class Graph:
  def __init__(self, graph_dict: Optional[dict] = None) -> None:
    self.dict = graph_dict or {}

  def add_vertix(self, vertix):
    if vertix not in self.dict:
      self.dict[vertix] = []

  def get_vertices(self) -> list:
    return list(self.dict.keys())

  def add_edge(self, edge: set) -> None:
    v1, v2 = tuple(edge)
    if v1 not in self.dict:
      self.add_vertix(v1)

    if v2 not in self.dict:
      self.add_vertix(v2)

    self.dict[v1].append(v2)
    self.dict[v2].append(v1)

  def get_edges(self) -> list:
    edges = []
    for vertix in self.dict:
      for next_vertix in self.dict[vertix]:
        if {next_vertix, vertix} not in edges:
          edges.append({next_vertix, vertix})

    return edges


def main():
  """
    a ------ c
    |        |
    |        |
    b ------ d ------ e
  """
  g = Graph()
  g.add_vertix("a")
  g.add_vertix("b")
  g.add_vertix("c")
  g.add_vertix("d")

  g.add_edge({"a", "b"})
  g.add_edge({"b", "c"})
  g.add_edge({"c", "d"})
  g.add_edge({"e", "d"})
  print(g.get_vertices())
  print(g.get_edges())

if __name__ == "__main__":
  main()
