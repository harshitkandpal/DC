package DC.P9;

import java.util.Scanner;

public class DynamicLoadBalancing {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of servers: ");
        int n = sc.nextInt();

        int[] load = new int[n];

        // Input current load
        System.out.println("Enter current load on each server:");
        for (int i = 0; i < n; i++) {
            System.out.print("Server " + (i + 1) + ": ");
            load[i] = sc.nextInt();
        }

        System.out.print("Enter number of incoming tasks: ");
        int tasks = sc.nextInt();

        // Assign tasks dynamically
        for (int t = 1; t <= tasks; t++) {

            int minIndex = 0;

            // Find least loaded server
            for (int i = 1; i < n; i++) {
                if (load[i] < load[minIndex]) {
                    minIndex = i;
                }
            }

            // Assign task
            load[minIndex]++;

            System.out.println("Task " + t +
                    " assigned to Server " + (minIndex + 1));
        }

        // Final load
        System.out.println("\nFinal Server Loads:");
        for (int i = 0; i < n; i++) {
            System.out.println("Server " + (i + 1) +
                    " = " + load[i]);
        }

        sc.close();
    }
}