import sys
class DisjointSetUnion:
    def __init__(self,n: int):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,i: int) -> int:
        if self.parent[i]==i:
            return i
        # compresion de ruta: conectar nodo directo a raiz para futuras consultas
        self.parent[i]=self.find(self.parent[i])
        return self.parent[i]
    def union(self,i: int,j: int) -> bool:
        root_i=self.find(i)
        root_j=self.find(j)
        if root_i!=root_j:
            if self.rank[root_i]<self.rank[root_j]:
                self.parent[root_i]=root_j
            elif self.rank[root_i]>self.rank[root_j]:
                self.parent[root_j]=root_i
            else:
                self.parent[root_j]=root_i
                self.rank[root_i]+=1
            return True
        return False
def kruskal_mst(n: int,edges: list) -> tuple:
    # 1. Ordenar aristas por peso de menor a mayor
    # arista es tupla: (peso,nodo_origen,nodo_destino)
    edges.sort()
    dsu=DisjointSetUnion(n)
    mst_edges=[]
    total_min_cost=0
    for weight,u,v in edges:
        # 2. y 3. Intentar unir nodos. Con exito, no hay ciclo.
        if dsu.union(u,v):
            total_min_cost+=weight
            mst_edges.append((u,v,weight))
            # un MST en un grafo de N nodos siempre tiene N-1 aristas
            if len(mst_edges)==n-1:
                break
    return total_min_cost,mst_edges
def main():
    edges_list=[(4,0,1),(4,0,2),(2,1,2),(3,1,3),(2,1,4),(3,2,4),(3,3,4)]
    num_nodes=5
    costo_minimo,arbol_resultado=kruskal_mst(num_nodes,edges_list)
    print(f"Costo minimo total para conectar la red: {costo_minimo}")
    print("Aristas seleccionadas para el arbol de expansion:")
    for u,v,w in arbol_resultado:
        print(f"  Nodo {u} <---> Nodo {v} | Costo (Peso): {w}")
if __name__=="__main__":
    main()