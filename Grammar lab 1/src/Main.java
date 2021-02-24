import java.util.HashMap;
import java.util.ArrayList;
import java.util.*;


    public class Main {
        public static Map<String, List<String>> Rules = new HashMap<String, List<String>>();

        String compar = "S";
        String input = "abaabb";


        public static void main(String[] args) {
            Rules.put("S", new ArrayList<String>(Arrays.asList("aA")));
            Rules.put("A", new ArrayList<String>(Arrays.asList("bS", "aB")));
            Rules.put("B", new ArrayList<String>(Arrays.asList("bC", "aB")));
            Rules.put("C", new ArrayList<String>(Arrays.asList("aA", "b")));

            Main main = new Main();
            main.cycle();


            System.out.println(Arrays.asList(Rules));
            System.out.println(Rules.values());
            System.out.println(Arrays.toString(Rules.keySet().toArray()));


        }


        public void cycle() {
            for (int i = 0; i < input.length(); i++) {
                while (i < input.length()) {
                    if (Arrays.toString(Rules.keySet().toArray()).contains("S")&& compar.contains("S") && input.charAt(i) == 'a') {//0
                        compar = compar.replace("S", "aA");
                        i++;
                      System.out.println("\t" + compar);

                    }
                    if (Arrays.toString(Rules.keySet().toArray()).contains("A") && compar.contains("A") && input.charAt(i) == 'b') { //1
                        compar = compar.replace("A", "bS");
                        i++;
                        System.out.println("\t" + compar);
                    } else if(Arrays.toString(Rules.keySet().toArray()).contains("A") && compar.contains("A") && input.charAt(i) == 'a'){
                        compar = compar.replace("A", "aB");
                    i++;
                    }
                    System.out.println("\t" + compar);
                    if (Arrays.toString(Rules.keySet().toArray()).contains("B") && compar.contains("B") && input.charAt(i) == 'b') {//2
                        compar = compar.replace("B", "bC");
                        i++;
                        System.out.println("\t" + compar);
                    } else if(Arrays.toString(Rules.keySet().toArray()).contains("B") && compar.contains("B") && input.charAt(i) == 'a'){
                        compar = compar.replace("B", "aB");
                        i++;
                        System.out.println("\t" + compar);
                    }
                    if (Arrays.toString(Rules.keySet().toArray()).contains("C") && compar.contains("C") && input.charAt(i) == 'a') { //3
                        compar = compar.replace("C", "aA");
                        i++;
                        System.out.println("\t" + compar);
                    } else if(Arrays.toString(Rules.keySet().toArray()).contains("C") && compar.contains("C") && input.charAt(i) == 'b'){
                        compar = compar.replace("C", "b");
                        i++;
                        System.out.println("\t" + compar);
                    }
                    if (compar.endsWith("S") || compar.endsWith("A") || compar.endsWith("B") || compar.endsWith("C")) {
                        System.out.println("Se termina");
                    }
                    if (compar.equals(input)) {
                        System.out.println("Este egal");
                        return;
                    }
                }
            }
        }
    }




/////////////////////////////////////////////////////////////


