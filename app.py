import pyautogui
import time
import random
import string

code = '''

import java.util.Scanner;
import java.text.DecimalFormat;

public class ex31 {
public static void main(String[] args) {
        
Scanner sc = new Scanner(System.in);
int U = sc.nextInt();
 double bill;
if (U <= 25) {
bill = U * 1.25;
     }
 else if (U <= 50) {
     bill = U * 1.45;
  }
  else if (U <= 75) {
 bill = U * 1.65;
       }
  else if (U <= 95) {
 bill = U * 1.95;
      }
  else {
  bill = U * 2.00;
      }
 DecimalFormat dc=new DecimalFormat("0.0#");
   System.out.printf("$ "+dc.format(bill));
        
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
