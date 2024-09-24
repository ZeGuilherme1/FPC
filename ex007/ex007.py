import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# grid size 
N = 100

# initial random grid
p0, p1 = 0.8, 0.2
grid = np.random.choice([0, 1], N*N, p=[p0, p1]).reshape(N, N)


def update(frameNum, img, grid):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # conta os vizinhos vivos
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                          grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                          grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                          grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))

            # regras do jogo
            if grid[i, j] == 1:  # célula tá viva
                if total < 2 or total > 3:
                    newGrid[i, j] = 0  # morre
            else:  
                if total == 3:
                    newGrid[i, j] = 1  

    img.set_array(newGrid)
    grid[:] = newGrid
    plt.title(f"Conway Game of Life - Frame {frameNum}")
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=1000, repeat=False)
plt.show()

