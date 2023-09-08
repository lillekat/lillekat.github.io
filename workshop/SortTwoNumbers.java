import java.util.Scanner;

/**
 * Write a description of class SortTwoNumbers here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class SortTwoNumbers
{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int a = s.nextInt();
        int b = s.nextInt();
        
        if(a > b) {
            System.out.println(b + " " + a);
        } else {
            System.out.println(a + " " + b);
        }
    }
}
