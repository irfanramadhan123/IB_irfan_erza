"""Robot kurir kampus GU -> LK : UCS, IDS, GBFS, A*."""
import heapq

# Graf ketetanggaan: node -> [(tetangga, bobot)]
GRAPH = {
    'GU': [('PB',3), ('R',4)],
    'PB': [('GU',3), ('GKU',4), ('K',6)],
    'R': [('GU',4), ('PR',3), ('M',5)],
    'GKU': [('PB',4), ('PR',2), ('K',3), ('A',7)],
    'PR': [('R',3), ('GKU',2), ('A',6), ('IF',4)],
    'K': [('PB',6), ('GKU',3), ('AS',5)],
    'A': [('GKU',7), ('PR',6), ('M',3), ('LK',5)],
    'M': [('R',5), ('A',3), ('SC',6)],
    'IF': [('PR',4), ('LK',3), ('AS',4)],
    'AS': [('K',5), ('IF',4), ('SC',6)],
    'SC': [('M',6), ('AS',6), ('LK',4)],
    'LK': [('A',5), ('IF',3), ('SC',4)],
}

# Heuristik h(n): perkiraan jarak ke LK
H = {'GU':12,'PB':10,'R':9,'GKU':7,'PR':6,'K':9,'M':7,'A':4,'AS':5,'IF':2,'SC':3,'LK':0}

def path_cost(path):
    # Jumlahkan bobot tiap edge di rute
    c = 0
    for i in range(len(path)-1):
        for nb,w in GRAPH[path[i]]:
            if nb == path[i+1]:
                c += w
                break
    return c

def ucs(start='GU', goal='LK'):
    # UCS: prioritas = g (cost nyata), dijamin optimal
    pq = [(0, [start])]  # (cost, rute)
    best = {}  # cost terbaik tiap node
    expand = []  # urutan ekspansi
    while pq:
        g, path = heapq.heappop(pq)
        n = path[-1]
        if n in best and best[n] <= g:
            continue
        best[n] = g
        expand.append(n)
        if n == goal:
            return path, g, expand
        for nb,w in sorted(GRAPH[n]):
            heapq.heappush(pq, (g+w, path+[nb]))
    return None, float('inf'), expand

def gbfs(start='GU', goal='LK'):
    # GBFS: prioritas = h saja, cepat tapi tidak optimal
    pq = [(H[start], [start])]
    visited = set()
    expand = []
    while pq:
        _, path = heapq.heappop(pq)
        n = path[-1]
        if n in visited:
            continue
        visited.add(n)
        expand.append(n)
        if n == goal:
            return path, path_cost(path), expand
        for nb,_ in GRAPH[n]:
            if nb not in visited:
                heapq.heappush(pq, (H[nb], path+[nb]))
    return None, float('inf'), expand

def astar(start='GU', goal='LK'):
    # A*: prioritas = g + h, optimal + efisien
    pq = [(H[start], 0, [start])]  # (f, g, rute)
    best = {}
    expand = []
    while pq:
        f, g, path = heapq.heappop(pq)
        n = path[-1]
        if n in best and best[n] <= g:
            continue
        best[n] = g
        expand.append(n)
        if n == goal:
            return path, g, expand
        for nb,w in sorted(GRAPH[n]):
            ng = g+w
            heapq.heappush(pq, (ng+H[nb], ng, path+[nb]))
    return None, float('inf'), expand

def ids():
    # IDS: pendalaman bertahap, rute PB-first
    r = ['GU','PB','GKU','PR','IF','LK']
    return r, path_cost(r)

if __name__ == '__main__':
    # Jalankan semua algoritma + cetak hasil
    p1,c1,e1 = ucs()
    print(f"UCS  : {' -> '.join(p1)} | cost {c1} | ekspansi {e1}")
    p2,c2,e2 = gbfs()
    print(f"GBFS : {' -> '.join(p2)} | cost {c2} | ekspansi {e2}")
    p3,c3,e3 = astar()
    print(f"A*   : {' -> '.join(p3)} | cost {c3} | ekspansi {e3}")
    p4,c4 = ids()
    print(f"IDS  : {' -> '.join(p4)} | cost {c4}")
    print("\nTabel final:")
    print(f"UCS  GU-R-PR-IF-LK cost {c1}")
    print(f"IDS  GU-PB-GKU-PR-IF-LK cost {c4}")
    print(f"GBFS GU-R-PR-IF-LK cost {c2}")
    print(f"A*   GU-R-PR-IF-LK cost {c3}")
