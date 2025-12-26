import pyautogui
import time
import random
import string

code = '''

import java.util.Scanner;

public class GCD{
public static void main(String[] args){
Scanner sc=new Scanner(System.in);

String input=sc.nextLine();
String[] values=input.split(",");

int N1=Integer.parseInt(values[0].trim());
int N2=Integer.parseInt(values[1].trim());

while(N2!=0){
int temp=N2;
N2=N1%N2;
N1=temp;
}

System.out.println(N1);
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
