import java.util.Arrays;
import java.util.Scanner;

public class CasesarCipher {
        static String[] alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        static char[] messageCharArray = {};
    
        public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter in a message to be encrypted using the Casesar Cipher: ");
    
        String message = scan.nextLine();
        message.toLowerCase();
        System.out.println("Your message is: " + message);

        traverseString(message);
        System.out.println(messageCharArray);

        // Trying to append each letter to an array
        // for (int i=0; i <= message.length(); i++) {
        //   char letter = message.charAt(i);
        //   messageCharArray.append(Arrays.toString(letter));
        // }
        // System.out.println(messageCharArray);
        
        
        System.out.println("How many times do you want to shift the letters by (negative number for left, positive number for right):");
        String shift = scan.nextLine();
        System.out.println("The amount your shifting each letter by is: " + shift);
        scan.close();

        
      }


      static void traverseString(String str)
      {
          for (int i = 0; i < str.length(); i++) {
              System.out.print(str.charAt(i) + " ");
              char letter = str.charAt(i);
              messageCharArray[i] = letter;
          }
      }
    } 
