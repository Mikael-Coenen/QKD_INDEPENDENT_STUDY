import java.util.Scanner;

public class CasesarCipher {
        static String[] alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        int letterPosition = alphabet.
    
        public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter in a message to be encrypted using the Casesar Cipher: ");
    
        String message = scan.nextLine();
        System.out.println("Your message is: " + message);
        
        System.out.println("How many times do you want to shift the letters by (negative number for left, positive number for right):");
        String shift = scan.nextLine();
        System.out.println("The amount your shifting each letter by is: " + shift);
        scan.close();
      }
    
      
      
    } 
