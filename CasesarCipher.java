import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class CasesarCipher {
        static char[] alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        static ArrayList<Character> messageCharArray = new ArrayList<Character>();
            
                public static void main(String[] args) {
                Scanner scan = new Scanner(System.in);
                System.out.println("Enter in a message to be encrypted using the Casesar Cipher: ");
            
                String message = scan.nextLine();
                message.toLowerCase();
                System.out.println("Your message is: " + message);
        
                traverseString(message);
                System.out.println(messageCharArray);   
                
                System.out.println("How many times do you want to shift the letters by (negative number for left, positive number for right):");
                String shift = scan.nextLine();
                System.out.println("The amount your shifting each letter by is: " + shift);
                scan.close();
                
              }
        
              static void traverseString(String str) {
                  for (int i = 0; i < str.length(); i++) {
                      char letter = str.charAt(i);
                      System.out.print(letter + " ");
                      messageCharArray.add(letter);
        }
      }

              static void assignValues(ArrayList<Character> arrayList) {
                for (char alphabetArray : messageCharArray) {
                  
                }             
              }
    } 
