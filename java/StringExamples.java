// String manipulation in Java
public class StringExamples {
    public static String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }

    public static boolean isAnagram(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int[] count = new int[256];
        for (char c : s1.toCharArray()) count[c]++;
        for (char c : s2.toCharArray()) {
            count[c]--;
            if (count[c] < 0) return false;
        }
        return true;
    }

    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);
            }
        }
        return prefix;
    }

    public static void main(String[] args) {
        System.out.println(reverse("Hello"));
        System.out.println("Anagram: " + isAnagram("listen", "silent"));
        System.out.println("Prefix: " + longestCommonPrefix(new String[]{"flower","flow","flight"}));
    }
}
