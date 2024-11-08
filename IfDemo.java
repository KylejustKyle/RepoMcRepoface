public class IfDemo {
    public static void main(String[] args) {
        int i = 5;
        int j = 8;

        if (i == 5) {
            System.out.println("I is 5");
        } else if (i == 5 && j == 8) {
            System.out.println("I is 5 and J is 8");
        } else if (j == 8) {
            System.out.println("J is 8");
        } else {
            System.out.println("Nothing matches. You suck bro.");
        }
    }
}
