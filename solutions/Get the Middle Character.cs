public class Kata
{
  public static string GetMiddle(string s)
  {
 if ( s==null || s.Length==0) return null;
 if(s.Length==1) return s;
 string res = "";
 int i = s.Length/2;
  if(s.Length % 2 !=0) res+=s[i];
 else {
 res+=s[i-1];
 res+=s[i];
 }
 return res;
  }
}