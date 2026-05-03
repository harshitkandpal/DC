package DC.P10;

import java.util.Scanner;

public class StaticLoadBalancing {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of servers: ");
        int n = sc.nextInt();

        int[] weights = new int[n];

        // Input weights
        System.out.println("Enter weight for each server:");
        for (int i = 0; i < n; i++) {
            System.out.print("Server " + (i + 1) + ": ");
            weights[i] = sc.nextInt();
        }

        System.out.print("Enter number of tasks: ");
        int tasks = sc.nextInt();

        // Build weighted sequence
        int totalWeight = 0;
        for (int i = 0; i < n; i++) {
            totalWeight += weights[i];
        }

        int[] sequence = new int[totalWeight];

        int index = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < weights[i]; j++) {
                sequence[index++] = i + 1;
            }
        }

        // Assign tasks
        System.out.println("\nTask Allocation:");
        for (int i = 0; i < tasks; i++) {
            System.out.println("Task " + (i + 1) +
                    " -> Server " + sequence[i % totalWeight]);
        }

        sc.close();
    }
}