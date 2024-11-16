from typing import List, Dict, Set

def has_cycle(graph: Dict[str, List[str]], node: str, visited: Set[str], path: Set[str]) -> bool:
    visited.add(node)
    path.add(node)
    
    if node in graph:
        for neighbor in graph[node]:
            if neighbor not in visited:
                if has_cycle(graph, neighbor, visited, path):
                    return True
            elif neighbor in path:
                return True
    
    path.remove(node)
    return False

def is_dag(nodes: List[dict], edges: List[dict]) -> bool:
    graph = {}
    
    for node in nodes:
        graph[node['id']] = []
    
    for edge in edges:
        source = edge['source']
        target = edge['target']
        if source in graph:
            graph[source].append(target)
    
    visited = set()
    for node in graph:
        if node not in visited:
            path = set()
            if has_cycle(graph, node, visited, path):
                return False
    
    return True

def analyze_pipeline(nodes: List[dict], edges: List[dict]) -> dict:
    
    return {
        "num_nodes": len(nodes),
        "num_edges": len(edges),
        "is_dag": is_dag(nodes, edges)
    }