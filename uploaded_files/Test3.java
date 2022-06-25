import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test3 
{
	public static void main(String args[]) throws NumberFormatException, IOException
	{
			Rectangle r1=new Rectangle();
			System.out.println(r1.getArea());
			Circle c1=new Circle();
			System.out.println(c1.getArea());

    }
}

class Shape
{
	int breadth;
	int length;
	int radius;
	public void accept() throws NumberFormatException, IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the breadth and length ");
		breadth=Integer.parseInt(br.readLine());
		length=Integer.parseInt(br.readLine());
		
	}
	public void acceptr() throws NumberFormatException, IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the radius ");
		Integer.parseInt(br.readLine());
	}
}
class Rectangle extends Shape
{
	int getArea() throws NumberFormatException, IOException
	{
		accept();
		return length*breadth;
		
	}
}
class Circle extends Shape
{
	double getArea() throws NumberFormatException, IOException
	{
		acceptr();
		return 3.14*radius*radius;
		
	}
}

