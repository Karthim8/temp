import pyautogui
import time
import random
import string

code = '''
import java.util.Scanner;

public class Main {
public static void main(String[] args) {

Scanner sc = new Scanner(System.in);

int K = sc.nextInt();

if (K <= 5) {
System.out.println("$1");
}
else if (K <= 10) {
System.out.println("$2");
}
else if (K <= 30) {
System.out.println("$5");
}
else if (K <= 50) {
System.out.println("$8");
}
else if (K <= 80) {
System.out.println("$15");
}
else {
System.out.println("$30");
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
