package workshop;

import java.util.Scanner;

/**
 * Write a description of class OddEcho here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class oddecho
{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int numOfWords = s.nextInt();
        /*
        String s1 = s.next();
        String s2 = s.next();
        String s3 = s.next();
        String s4 = s.next();
        String s5 = s.next();
        
        System.out.println(s1);
        System.out.println(s3);
        System.out.println(s5);
         */
        boolean odd = true;

        while (numOfWords > 0) {
            String word = s.next();

            if (odd) {
                System.out.println(word);
            }

            odd = !odd;
            numOfWords = numOfWords - 1;
        }
    }
}
