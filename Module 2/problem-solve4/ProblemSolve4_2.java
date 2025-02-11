import java.util.Scanner;

public class ProblemSolve4_2 {
    /*
     * Asks the user for an age (integer).
     * If age >= 18, returns "You can vote".
     * If 0 <= age <= 17, returns "Too young to vote".
     * If age < 0, returns "You are a time traveler".
     */
    public static void main(String[] args) {

        // set up Scanner to capture user input
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your age: ");
        int age = input.nextInt();

        // Add code here
        if (age >= 18) {
            System.out.println("You can vote.");
        } else if (age >= 0 && age <= 17) {
            System.out.println("Too young to vote.");
        } else {
            System.out.println("You are a time traveler.");
        }

        input.close();
    }//end main

}//end class
