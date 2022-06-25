import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Email 
{
	public static void main(String args[]) throws IOException
	{
		try
		{
			BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Enter the email");
			String email=br.readLine();
			char ch=email.charAt(0);
			if(ch=='@')
			{
				System.out.println("Username is missing");
			}
			else
			{
				int p1=email.indexOf('@');
				if(p1!=-1)
				{
					int p2=email.indexOf('@',p1+1);
					if(p2!=-1)
					{
						System.out.println("Email ID having at least one @");
					}
					else
					{
						char ch1=email.charAt(p1+1);
						if(ch1=='.')
						{
							System.out.println("Domain name missing");
						}
						else
						{
							int p3=email.indexOf('.',p1+1);
							if((p3-p1)==6)
							{
								if((email.length()-p3)==4)
								{
									String badchr="!#$%^&*()?><";
									boolean flag=true;
									for(int i=0;i<email.length();i++)
									{
										int ch3=badchr.indexOf(email.charAt(i));
										if(ch3!=-1)
										{
											if(flag)
											{
												System.out.println("Following bad character");
												flag=false;
											}
											System.out.println(email.charAt(i));
										}
									}
									if(flag)
									{
										System.out.println("Well Done!!!");
									}
								
								}
								else
								{
									System.out.println("Server name is missing");
								}
							}
							else
							{
								System.out.println("Wrong domin name");
							}
						}
					}
				}
				else
				{
					System.out.println("Email ID having at least one @");
				}
			}
			
		}
		catch(Exception e)
		{
			System.out.println("Out of Boundry Exception");

		}
			
		}
		
}

