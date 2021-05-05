public static class Kata
{
  // return masked string
  public static string Maskify(string cc)
  {
   if(cc.Length < 4) return cc;
   string masked="";
   for(int i=0; i<cc.Length; i++){
   if ( i<cc.Length-4) masked+="#";
   else masked += cc[i];
   }
   return masked;
  }
}
