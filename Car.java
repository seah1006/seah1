package test;

public class Car {
	private final String model;
	
	public Car (String model) {
		this.model = model;
		
	}
	
	public String toString() {
		return model;
	}
	
	public boolean equals(Object obj) {
		if (this == obj) return true;
		
		if (!(obj instanceof Car)) return false;
		
		Car confignation = (Car) obj;
		
		return model.equals(confignation.model);
		
	}
	public static void main(String[] args) {
		

	}

}
