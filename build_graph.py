#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:16:45 2019

@author: wangxindi
"""

"""
This file is used to build a graph using given connections
"""

from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def find_value(self, node):
        if node == []:
            return None
        else:
            return_nodes = []
            for k, v in self._graph.items():
                if k in node:
                    node_list = list(v)
                    return_nodes = return_nodes + node_list
            return_nodes = set(return_nodes)
            return_nodes = list(return_nodes)
            return return_nodes
                    
    def find_node(self, given_node, distance):
        """ Find any partent/child node given nodeX and distance """
        stop_point = distance - 1
        if stop_point == 0:
            possible_nodes = self.find_value(given_node)
            return possible_nodes
        else:
            possible_nodes = self.find_value(given_node)
            new = self.find_node(possible_nodes, stop_point)
            new_nodes = list(possible_nodes) + list(new)
            new_nodes = set(new_nodes)
            return list(new_nodes)
        return None
    
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
    