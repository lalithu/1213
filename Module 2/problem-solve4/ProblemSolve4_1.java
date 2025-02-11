import java.util.Scanner;

public class ProblemSolve4_1 {

    // Display "odd" if the given integer n is odd, or "even" otherwise.
    public static void main(String[] args) {

        // set up Scanner to capture user input
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        // Add code here
        if (n % 2 == 0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }

        input.close();
    }//end main

}//end class
