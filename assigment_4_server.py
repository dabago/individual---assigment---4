#%%
from flask import Flask, jsonify, request


server = Flask("Graph Server")

graph = {"graph":None}


@server.route("/mygraph",  methods=["GET"])
def mygraph():
    if graph["graph"] == None:
        return jsonify("No graph uploaded. Please upload graph")
    
    else:
        return jsonify({"This is your current graph" : graph})
        
    

@server.route("/upload-graph", methods=["POST"])
def upload_graph():
    body = request.get_json()
    
    if type(body) == dict:
        
        if body == {}:
            return jsonify("Please upload a valid graph, not an empty one")

        if body.values() != None:
            values = body.values()
            for i in values:
                if type(i) != list:
                    return jsonify("Please upload a valid graph. Check values")
                
   
            graph ["graph"] = body
            return jsonify({"This is your graph":graph}) 
        
    else:
        return jsonify("Please upload a valid graph. It must be a dictionary")
    

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    
    if start or end not in graph.keys():
        return False
    
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for conn in graph[start]:
        if conn not in path:
            newpaths = find_all_paths(graph, conn, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# I am one Degree away from me as a basic concept. 
    
def degrees_of_separation(graph, start, end):
    all_paths = find_all_paths(graph, start, end)
    degrees = None
    
    for path in all_paths:
        steps = 0
        for step in path:
            steps += 1
        if degrees is None or steps < degrees:
            degrees = steps   
    return degrees


@server.route("/degrees-of-separation/<origin>/<destination>") 
def getting_degrees(origin, destination):
    if graph["graph"] == None:
        return jsonify ("No  graph uploaded. Please upload graph")
    else:
        degrees = degrees_of_separation(graph["graph"], origin, destination)
        if degrees == None:
            return jsonify ("There is no connection")
        else:
            return jsonify({"The degree/s of separation is/are":degrees})
        
            










server.run()

