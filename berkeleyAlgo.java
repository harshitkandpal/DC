package DC;

import java.util.Scanner;

public class berkeleyAlgo{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter the number no of notes");
        int no_of_nodes = sc.nextInt();
        int[] nodes_time = new int[no_of_nodes];

        int sum =0;
        for(int i=0;i<no_of_nodes;i++){
            System.out.print("Enter time for node"+i+1+" : ");
            nodes_time[i] = sc.nextInt();
            sum += nodes_time[i];
        }

                        int average = sum/no_of_nodes;
        System.out.println("\nThe avg time: "+average);
    }
}