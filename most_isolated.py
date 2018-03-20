#!/usr/bin/python3
#
# Author:	Mike Vasiljevs
# Created:	19/march/2018
# 
# A solution to "the most isolated feature" coding exercise
#
import numpy as np
from scipy.spatial import Delaunay
import sys

# Get index of the most isolated point
def maxIsolationIdx(points):
	# 1) Compute the Delaunay triangulation, which tells us about the connections between the points as the centres of the Voronoi Diagram cells
	triangulation = Delaunay(points)
	# Neighbouring vertex indices: offsets and indices to neighbours,
	#	@sa https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.spatial.Delaunay.vertex_neighbor_vertices.html#scipy.spatial.Delaunay.vertex_neighbor_vertices
	neibor_idx_offsets, neibor_idxs = triangulation.vertex_neighbor_vertices
	
	# 2) Compute the isolation distances for each point. Isolation distance is how close the nearest neighbouring point is.
	isolation_distances = []
	# Loop through points...
	for i in np.arange(0, len(points)):
		neibor_distances = []
		# for each neighbour index...
		for neibor_idx in neibor_idxs[neibor_idx_offsets[i]:neibor_idx_offsets[i+1]]:
			# calculate distance from the current point to a neighbour 
			distance = np.linalg.norm(points[neibor_idx] - points[i])
			neibor_distances.append(distance)
		# store the nearest distance as the isolation distance
		min_distance = min(neibor_distances)
		isolation_distances.append(min_distance)

	# 3) Find the index of the most isolated element and return it
	most_isolated_idx = isolation_distances.index(max(isolation_distances))
	return most_isolated_idx

# Read name and point data in the format "name x y"
def readPointsFromStdin():
	names = []
	points = []
	lines = sys.stdin.readlines()
	for l in lines:
		data = l.split()
		names.append( data[0] )
		x,y = float(data[1]), float(data[2])
		points.append(np.array([x, y]))
	return points,names

def main():
	# Read feature data
	feature_points, feature_names = readPointsFromStdin()

	# Compute the index of the most isolated feature
	idx = maxIsolationIdx(feature_points)
	
	# ...print its name
	print (feature_names[idx])
	
main()

