// Recursion Examples in Java
public class RecursionExamples {
    public static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }

    public static int sumOfDigits(int n) {
        if (n == 0) return 0;
        return n % 10 + sumOfDigits(n / 10);
    }

    public static boolean isPalindrome(String s) {
        if (s.length() <= 1) return true;
        if (s.charAt(0) != s.charAt(s.length() - 1)) return false;
        return isPalindrome(s.substring(1, s.length() - 1));
    }

    public static void main(String[] args) {
        System.out.println("5! = " + factorial(5));
        System.out.println("Sum of digits of 12345: " + sumOfDigits(12345));
        System.out.println("'racecar' palindrome: " + isPalindrome("racecar"));
        System.out.println("'hello' palindrome: " + isPalindrome("hello"));
    }
}
