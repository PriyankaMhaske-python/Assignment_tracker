
public class Test4 
{
	public static void main(String args[])
	{
		
	}

}
class S
{
	int l,b,r;
	S(int l,int b,int r)
	{
		this.l=l;
		this.b=b;
		this.r=r;
		display();
	}
	private void display() 
	{
		System.out.println("l"+l);
		System.out.println("b"+b);
		System.out.println("r"+r);
		
	}
}
class R1 extends S
{
	
	R1(int l, int b, int r) 
	{
		super(l, b, r);
		
		
	}

	
}
