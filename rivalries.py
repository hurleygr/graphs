def rivalries():
    """
    Determines if it is possible to separate a list of people into two separate groups
    based on a list of rivalries between some of the people. Returns yes and possible groups if so, no otherwise.
    """
    from collections import defaultdict
    file_name = input("Enter name of file input:  ")
    in_file = open(file_name, 'r')
    graph = defaultdict(list)
    players = []
    visited = set()
    ans = ""
    line = in_file.readline()
    line = in_file.readline().strip()
    # Gets list of players from input
    while not line.isnumeric():
        players.append(line)
        line = in_file.readline().strip()
    line = in_file.readline().strip().split()
    # Creates graph of edges between rivals
    while line:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
        line = in_file.readline().strip().split()

    beavers = set()
    ducks = set()
    q = [list(graph.keys())[0]]
    # breadth first search starting from first rival
    while q:
        next_q = []
        for vertex in q:
            if vertex in visited: continue
            visited.add(vertex)
            beaver_rival = any([x in beavers for x in graph[vertex]])
            duck_rival = any([x in ducks for x in graph[vertex]])
            # if player is in a team, check that rivals aren't on same team
            if vertex in beavers:
                if beaver_rival:
                    ans = "No"
                    break
                else:
                    for rival in graph[vertex]: # add all rivals to other team
                        ducks.add(rival)
                        if rival not in visited:
                            next_q.append(rival)
            elif vertex in ducks:
                if duck_rival:
                    ans = "No"
                    break
                else:
                    for rival in graph[vertex]:
                        beavers.add(rival)
                        if rival not in visited:
                            next_q.append(rival)
            else:
                if beaver_rival:
                    if duck_rival:
                        ans = "No"
                        break
                    else:
                        ducks.add(vertex)
                        for rival in graph[vertex]:
                            beavers.add(rival)
                            if rival not in visited:
                                next_q.append(rival)
                else:
                    beavers.add(vertex)
                    for rival in graph[vertex]:
                        ducks.add(rival)
                        if rival not in visited:
                            next_q.append(rival)
        q = next_q
    if ans == "No":
        print(ans)
    else:

        b_string = "Beavers: "
        d_string = "Ducks: "
        for x in beavers:
            b_string += x
            b_string += " "
        for x in ducks:
            d_string += x
            d_string += " "
        # deals with isolated vertices
        for missed in players:
            if missed not in visited:
                b_string += missed
                visited.add(missed)
                for rival in graph[missed]:
                    if rival not in visited:
                        visited.add(rival)
                        d_string += rival
                        d_string += " "
                b_string += " "
        print("Yes")
        print(b_string)
        print(d_string)
rivalries()
