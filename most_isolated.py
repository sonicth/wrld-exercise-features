
import numpy as np
from scipy.spatial import Delaunay

from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys

# get index of the most isolated point
def isolationIdx(points):
	# 1) compute Delaunay triangulation, which tells us about the connections between centres of the Voronoi Diagram cells
	# print ("* computing delaunay")
	tri = Delaunay(points)

	# 2) compute isolation distances for each point. Isolation distance is how close the nearest neighbouring point is.
	# Neighbouring vertex indices: offsets and indices to neighbours,
	#	@sa https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.spatial.Delaunay.vertex_neighbor_vertices.html#scipy.spatial.Delaunay.vertex_neighbor_vertices
	neibor_idx_offsets, neibor_idxs = tri.vertex_neighbor_vertices
	isolation_distances = []
	# print ("* computing distances")
	# loop through points...
	for i in np.arange(0, len(points)):
		neibor_distances = []
		# for each neighbour index...
		for neibor_idx in neibor_idxs[neibor_idx_offsets[i]:neibor_idx_offsets[i+1]]:
			# calculate current point to neighbour distance
			distance = np.linalg.norm(points[neibor_idx] - points[i])
			neibor_distances.append(distance)
		# store the nearest distance as the isolation distance
		min_distance = min(neibor_distances)
		isolation_distances.append(min_distance)

	# print ("* done!")
	#find element index, which is furthest from any other element,
	# 	i.e. the one that has the largest of isolation or the minimum neighbour distances
	most_isolated_idx = isolation_distances.index(max(isolation_distances))
	return most_isolated_idx

# read name and point data in the format "name x y"
def readPointsFromStdin():
	names = []
	points = []
	lines = sys.stdin.readlines()
	for l in lines:
		data = l.split()
		names.append( data[0] )
		x,y = float(data[1]), float(data[2])
		points.append(np.array([x, y]))
	# print ("**line ", data)
	return points,names

def main():
	# read feature data
	feature_points, feature_names = readPointsFromStdin()

	# compute index of most isolated feature
	idx = isolationIdx(feature_points)
	
	# ...print its name
	print (feature_names[idx])

	# DBGG
	# sys.exit(0)
	# y = np.array([2, 3])
	# xs = []
	# ys = []
	# plt.scatter(xs, ys)
	# plt.scatter(xs[i], ys[i])
	# plt.show()

main()

