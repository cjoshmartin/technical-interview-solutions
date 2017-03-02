public class Test {

	/**
	 * @param args
	 */

	private static String output =" ";
 	
	public static int fib(int n){
		if (n==0)
			return 0;
		else if(n==1)
			return 1;
		else
			return fib(n-2)+fib(n-1);
	}
	public static void main(String[] args){
	      int n=14;
	     for(int i=0;i<n;i++){
	    	System.out.print( "" + fib(i)+ " ");
	     }
	     System.out.println("\nThe sum is "+ fib(n-1));
	 }// end of main
}
