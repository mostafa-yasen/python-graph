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

  def bfs(self, start: any, end: any) -> list:
    visited  = list()
    queue = [[start]]

    while queue:
      path = queue.pop(0)
      node = path[-1]
      if node in visited:
        continue

      visited.append(node)
      if node == end:
        return path

      adjacent_nodes = self.dict.get(node, [])
      for adjacent_node in adjacent_nodes:
        new_path = path[:]
        new_path.append(adjacent_node)
        queue.append(new_path)

  def dfs(self, start: any, end: any) -> list:
    visited  = list()
    stack = [[start]]

    while stack:
      path = stack.pop()
      node = path[-1]
      if node in visited:
        continue

      visited.append(node)
      if node == end:
        return path

      adjacent_nodes = self.dict.get(node, [])
      for adjacent_node in adjacent_nodes:
        new_path = path[:]
        new_path.append(adjacent_node)
        stack.append(new_path)

def main():
  """
    a ------ c     f   g
    |    /  |  \  | \  |
    |  /    |   \ |  \ |
    b ----- d -- e    h
  """
  g = Graph()
  g.add_vertix("a")
  g.add_vertix("b")
  g.add_vertix("c")
  g.add_vertix("d")
  g.add_vertix("e")
  g.add_vertix("f")
  g.add_vertix("g")
  g.add_vertix("h")

  g.add_edge({"a", "b"})
  g.add_edge({"a", "c"})

  g.add_edge({"b", "c"})
  g.add_edge({"b", "d"})

  g.add_edge({"c", "d"})
  g.add_edge({"c", "e"})

  g.add_edge({"d", "e"})

  g.add_edge({"e", "f"})
  
  g.add_edge({"h", "f"})
  
  g.add_edge({"g", "h"})

  # print(g.get_vertices())
  # print(g.get_edges())
  print("BFS: ", g.bfs("b", "g"))
  print("DFS: ", g.dfs("b", "g"))

if __name__ == "__main__":
  main()
