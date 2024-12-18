import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class CasesarCipher {
  // Char array of the alphabet
  static char[] alphabet = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };

  // Array of each character in their message as an array
  static ArrayList<Character> messageCharArray = new ArrayList<Character>();

  // User message as string
  static String message;

  public static void main(String[] args) {
    // Scan for user message
    Scanner scan = new Scanner(System.in);

    // Ask user to enter message
    System.out.println("Enter in a message to be encrypted using the Casesar Cipher: ");

    message = scan.nextLine();

    // Clean message
    message = message.toLowerCase().strip();
    

    // Trying to user-proof 
    for (int i = 0; i < message.length(); i++) {
      for (char letter : alphabet) {
        if (letter != message.indexOf(i)) {
          System.out.println("You must input only characters from the alphabet for your message.");
          message = scan.nextLine();
        }
      }
    }
    for (int j = 0; j < message.length(); j++) {
      char letterInMessage = (char) message.indexOf(j);
      for (int i = 0; i < alphabet.length; i++) {
        char letterInAlphabet = alphabet[i];
        if (letterInAlphabet != letterInMessage) {
          System.out.println("You must input only characters from the alphabet for your message.");
          message = scan.nextLine();
        }

  
    // Convert message to lower case
    message = message.toLowerCase();

    // Tell user their message
    System.out.println("Your message is: " + message);

    // Traverse message
    traverseString(message);

    // Ask user how many times they want to shift each character in the message
    System.out.println(
        "How many times do you want to shift the letters by (negative number for left, positive number for right):");
    Integer shift = scan.nextInt();
    System.out.println("The amount your shifting each letter by is: " + shift);

    // Call assignvalues on message char array and add the shift
    assignValues(messageCharArray, shift);
    System.out.println(text);

    // Close scanner
    scan.close();
  }
}
  }

  // Add each character in a message to an arraylist
  static void traverseString(String str) {
    for (int i = 0; i < str.length(); i++) {
      char letter = str.charAt(i);
      messageCharArray.add(letter);
    }
  }

  // Create empty text that will have shifted letters
  static String text = "";

  static void assignValues(ArrayList<Character> arrayList, Integer shifter) {
    // Loop through the leters in a message
    for (int j = 0; j < arrayList.size(); j++) {
      char letterInMessage = arrayList.get(j);
      // Loop through the leters in the alphabet
      for (int i = 0; i < alphabet.length; i++) {
        char letterInAlphabet = alphabet[i];
        if (letterInAlphabet == letterInMessage) {
          // If the user asks to go up from z, loop them back to a
          if (letterInAlphabet == 'z') {
            text += alphabet[(26 - (27 - shifter))];
            continue;
          }
          // If the user asks to go down from a loop them back to z
          else if (letterInAlphabet == 'a' && shifter <= -1) {
            text += alphabet[(26 + shifter)];
            continue;
          }
          // Add the shifted letter to their new message
          else {
            text += alphabet[i + shifter];
            continue;
          }
        }
      }
    }
  }
}
