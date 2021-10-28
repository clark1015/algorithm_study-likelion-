import java.util.*;

public class Practice {
	public static boolean solution(String s) {
		boolean answer = true;
		int s_len = s.length();
		if ((s_len == 4) || (s_len == 6)){
			for(int i = 0; i < s_len; i++) {
				char tmp = s.charAt(i);
				if(Character.isDigit(tmp) == false) {
					answer = false;
				}
			}
			
		}
		else {
			answer = false;
		}
		
		return answer;
	}
public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	String str = scanner.next();
	System.out.println(solution(str));
}
}
