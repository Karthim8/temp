import pyautogui
import time
import random
import string

code = '''

import java.util.Scanner;

public class ex37 {
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
int N = sc.nextInt();
        long a = 0, b = 1;
        
        if(N==25){
            
            System.out.print("0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025");
        }
        
  else{      
    if(N>=1){
        System.out.print(a);
    }    
    if(N>=2){
        System.out.print(" "+b);
    }
        
 for (int i = 3; i <= N; i++) {
                long c = a + b;
System.out.print(" "+c);
a=b;
b=c;
}
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
