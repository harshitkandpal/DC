package DC.P6;

import java.util.Scanner;

public class RicartAgrawala {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        System.out.print("Enter process requesting Critical Section: ");
        int requester = sc.nextInt();

        // Validate requester
        if (requester < 1 || requester > n) {
            System.out.println("Invalid process ID.");
            return;
        }

        System.out.println("\nProcess " + requester +
                " sends REQUEST to all other processes:\n");

        int replies = 0;

        // Send request to all
        for (int i = 1; i <= n; i++) {
            if (i != requester) {
                System.out.println("REQUEST sent from Process " +
                        requester + " to Process " + i);

                System.out.println("REPLY sent from Process " +
                        i + " to Process " + requester);

                replies++;
            }
        }

        // Check all replies
        if (replies == n - 1) {
            System.out.println("\nAll replies received.");
            System.out.println("Process " + requester +
                    " enters Critical Section.");
        }

        // Exit section
        System.out.println("Process " + requester +
                " exits Critical Section.");

        // Release
        System.out.println("Process " + requester +
                " sends RELEASE to all processes.");

        sc.close();
    }
}