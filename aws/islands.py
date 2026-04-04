def numIslands(grid) -> int:
  if not grid:
    return 0

  rows, cols = len(grid), len(grid[0])
  num_islands = 0

  def dfs(i, j):
    # Validaciones
    if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
      return

    # Marcar como visitado
    grid[i][j] = "0"

    # Explorar vecinos
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == "1":
        num_islands += 1
        dfs(i, j)

  return num_islands


grid = [
["1","1","0","0"],
["1","1","0","0"],
["0","0","1","0"],
["0","0","0","1"]
]

print(numIslands(grid))