import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class CasesarCipher {
  static char[] alphabet = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };

  // Array of each character in an array
  static ArrayList<Character> messageCharArray = new ArrayList<Character>();

  // Array of each character in an arrayList
  static ArrayList<Integer> valueOfCharInMessage = new ArrayList<Integer>();

  static String message;

  public static void main(String[] args) {
    // Ask user for message
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter in a message to be encrypted using the Casesar Cipher: ");
    message = scan.nextLine();

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

    assignValues(messageCharArray, shift);
    System.out.println(text);

    scan.close();
  }

  // Add each character in a message to an arraylist
  static void traverseString(String str) {
    for (int i = 0; i < str.length(); i++) {
      char letter = str.charAt(i);
      messageCharArray.add(letter);
    }
  }

  static String text = "";
    static void assignValues(ArrayList<Character> arrayList, Integer shifter) {
      for (int j = 0; j < arrayList.size(); j++) {
        char letterInMessage = arrayList.get(j);
        for (int i = 0; i < alphabet.length; i++) {
          char letterInAlphabet = alphabet[i];
          if (letterInAlphabet == letterInMessage) {
            // If the user asks for z loop them back to a
            if (letterInAlphabet == 'z') {
              text += alphabet[(26-(27-shifter))];
              continue;
            }
            else if (letterInAlphabet == 'a' && shifter <= -1) {
              text += alphabet[(26+shifter)];
              continue;
            }
            else {
              text += alphabet[i + shifter];
              continue;
            }
        }
      }
    }
  }
}