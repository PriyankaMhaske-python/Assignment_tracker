
public class Test2 
{
      public static void main(String args[])
      {
    	  
    	   B b1 = new B();
    	 b1.display();
      }
}
class A
{
	void display()
	{
		System.out.println("class a");
	}
}
class B extends A
{
	
	void display()
	{ 
	    super.display();
		System.out.println("class b");
		
	}
}