package test;

import java.util.Date;
import java.text.MessageFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.StringTokenizer;

public class CarTest {

	public static void main(String[] args) {
		Car myCar = new Car("그랜저");
		Car yourCar = new Car("그랜저");
		
		StringTokenizer st = new StringTokenizer(yourCar.toString());
		
		Calendar cal = Calendar.getInstance();
		Date specificTime = cal.getTime();
		String equalsValue = "";
		if (myCar.equals(yourCar)) {equalsValue = "동일하다";}
		SimpleDateFormat sdf = new SimpleDateFormat("MM-dd-yyyy");
		String dateValue = sdf.format(specificTime);
		
//		String msf = MessageFormat.format("자동차 모델이 둘 다 [{1}]로 {0}.", equalsValue, st.nextToken());
		String msf2 = MessageFormat.format("날짜: {1}, 자동차 모델 = {0}, 운전자(홍길동)",myCar.toString(), dateValue);
		StringTokenizer st2 = new StringTokenizer(msf2, " ,=()");
		
//		System.out.println(msf);
		System.out.println(msf2);
		
		while (st2.hasMoreTokens()) {
			System.out.println(st2.nextToken());
		}

}
}
