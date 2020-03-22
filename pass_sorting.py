import os

way = os.getcwd()
file_way = os.path.join(way, "pList", "pb.txt")

sort_file = open(file_way, 'w')

passes = []

for line in sort_file:
    passes = line

print(passes)