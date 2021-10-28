import java.util.Scanner;

public class Plus {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int trial = scanner.nextInt();
		for(int i = 0; i < trial; i++) {
			int a = scanner.nextInt();
			int b = scanner.nextInt();
			System.out.println(a + b);
		}
	}
}
