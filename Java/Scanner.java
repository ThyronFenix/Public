package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int currentYear = 2024;
//        System.out.println(getInputFromConsole(currentYear));
        System.out.println(getInputFromScanner(currentYear));
    }

/*    public static String getInputFromConsole(int currentYear){
        String name = System.console().readLine("Hi, this is console input");
        System.out.println("Hi " + name + ", Thanks for taking the course");
        return "";
    }
*/
    public static String getInputFromScanner(int currentYear){
        Scanner scanner = new Scanner(System.in);
        System.out.println(" Hi!, what's your name? ");
        String name = scanner.nextLine();
        System.out.println("What year were you born? ");
        boolean validDOB = false;
        int age = 0;
        do{
            System.out.println("Enter a year of birth >= " + (currentYear - 125) + " and <= " + (currentYear));
            try {
                age = checkData(currentYear, scanner.nextLine());
                validDOB = age < 0 ? false : true;
            }catch (NumberFormatException badUserData){
                System.out.println("Characters not allowed! Try again.");
            }
        }while (!validDOB);
        return "So you are " + age + " years old";
    }

    public static int checkData(int currentYear, String dateOfBirth){
        int dob = Integer.parseInt(dateOfBirth);
        int minimumYear = currentYear - 125;

        if((dob < minimumYear) || (dob > currentYear)){
            return -1;
        }
        return (currentYear - dob);
    }
}
