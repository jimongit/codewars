using System;
using System.Collections.Generic;

public class Kata
{
  public static bool IsIsogram(string str) 
  {
  if(str==null || str.Length == 0) return true;
  str=str.ToLower();
  HashSet<Char> set = new HashSet<Char>();
   for(int i=0; i<str.Length;i++){   
   if (!set.Add(str[i])) return false; 
   }
   return true;
  }
}