# You are given an array, paths, where each element paths[i] = [cityAᵢ, cityBᵢ] represents a direct route from cityAᵢ to cityBᵢ. 
# Your task is to identify the final city on the route—the one that has no outgoing path to any other city. 
# The structure of the routes is guaranteed to be a simple chain without loops, so there will be exactly one such destination.
paths_a = [("London", "New York"), ("New York", "Lima"), ("Lima", "Sao Paulo")];
paths_b = [["B", "C"], ["D", "B"], ["C", "A"]];

def desCity(paths):
    n = len(paths);
    for i in range(n):
        candidate = paths[i][1];
        good = True;
        for j in range(n):
            if paths[j][0] == candidate:
                good = False;
                break;
        if good:
            return candidate;
    return "";

print(desCity(paths_a));
print(desCity(paths_b));