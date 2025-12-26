import pyautogui
import time
import random
import string

code = '''
import java.util.Scanner;

public class Main {
public static void main(String[] args) {

Scanner sc = new Scanner(System.in);

String I = sc.nextLine().trim();

if (I.equals("A")) {
System.out.println("5000");
}
else if (I.equals("B")) {
System.out.println("4500");
}
else if (I.equals("C")) {
System.out.println("3000");
}
else if (I.equals("D")) {
System.out.println("1500");
}
else if (I.equals("E")) {
System.out.println("500");
}

sc.close();
}
}

'''

print("Place cursor in editor. Typing starts in 7 seconds...")
time.sleep(7)

for char in code:
    # Decide whether to make a mistake (8% chance)
    if random.random() < 0.08 and char.isalnum():
        wrong_char = random.choice(string.ascii_letters)
        pyautogui.write(wrong_char)
        time.sleep(random.uniform(0.1, 0.25))
        pyautogui.press('backspace')
        time.sleep(random.uniform(0.05, 0.15))

    pyautogui.write(char)
    time.sleep(random.uniform(0.04, 0.12))
