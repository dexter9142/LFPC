import java.util.HashMap;
import java.util.LinkedList;

public class ntoDFA {
    static class Edge {
        int source;
        int destination;
        char weight;

        public Edge(int source, int destination, char weight) {
            this.source = source;
            this.destination = destination;
            this.weight = weight;
        }
    }

    static class Graph {
        int vertices;
        LinkedList<Edge> [] adjacencylist;
        HashMap<Edge, Integer> transCounter = new HashMap<>();

        Graph(int vertices) {
            this.vertices = vertices;
            adjacencylist = new LinkedList[vertices];
            //initialize adjacency lists for all the vertices
            for (int i = 0; i <vertices ; i++) {
                adjacencylist[i] = new LinkedList<>();
            }
        }

        public void addEgde(int source, int destination, char weight) {
            Edge edge = new Edge(source, destination, weight);
            transCounter.putIfAbsent(edge, 0);
            transCounter.put(edge, transCounter.get(edge)+1);
            System.out.println("tuta : " + transCounter.get(edge));
            adjacencylist[source].addFirst(edge); //for directed graph
        }

        public void printGraph(){
            for (int i = 0; i <vertices ; i++) {
                LinkedList<Edge> list = adjacencylist[i];
                for (int j = 0; j <list.size() ; j++) {
                    System.out.println("q" + i + " is connected to q" +
                            list.get(j).destination + " via char " +  list.get(j).weight);
                }
            }
        }

        public void printGraph2(){
            int vertices = 6;
            Graph graph1 = new Graph(vertices);
            for(int i= 0; i<vertices; i++){
                LinkedList<Edge> list2 = adjacencylist[i];
                for(int j = 0; j<list2.size(); j++) {
                    System.out.println(i + " " + list2.get(j).weight);
                    for(int k=0; k<list2.size(); k++){
                        if(k!=j && list2.get(j).weight == list2.get(k).weight){
                            System.out.println(list2.get(j).destination + " aaaa " + list2.get(j).destination);   //PROBLEME MARI
                        }
                    }
                }
            }
        }





    public static void main(String[] args) {
        int vertices = 6;
        Graph graph = new Graph(vertices);
        graph.addEgde(0, 0, 'a');
        graph.addEgde(0, 1, 'a');
        graph.addEgde(1, 1, 'a');
        graph.addEgde(1, 3, 'b');
        graph.addEgde(0, 2, 'b');
        graph.addEgde(1, 2, 'c');
        graph.addEgde(2, 3, 'b');
        graph.printGraph();
        graph.printGraph2();
    }


    }


}