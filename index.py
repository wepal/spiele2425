import os

for i in range(100):
    with open(f"file_{i}.txt", "w") as f:
        f.write(f"Hello this is file {i}")

