import java.util.Scanner;

public class ProblemSolve4_3 {

    /*
     * Calculates final weekly pay given hours worked and hourly wage,
     * paying time-and-a-half for any hours > 40.
     *
     */
    public static void main(String[] args) {

        // set up Scanner to capture user input
        Scanner input = new Scanner(System.in);
        
        // Read the number of hours worked and hourly wage from the user
        int hours = input.nextInt(); // Input for hours worked
        double wage = input.nextDouble(); // Input for hourly wage
        
        double totalPay; // Variable to store the total weekly pay

        // Calculate total pay based on hours worked
        if (hours <= 40) {
            // Regular pay calculation if hours worked are 40 or less
            totalPay = hours * wage;
        } else {
            // Regular pay for the first 40 hours + overtime pay for hours above 40
            totalPay = (40 * wage) + ((hours - 40) * (wage * 1.5));
        }

        // Output the total weekly pay
        System.out.println("Final weekly pay: $" + totalPay);

        // Close the scanner object to prevent resource leak
        input.close();
    } // end main

} // end class
