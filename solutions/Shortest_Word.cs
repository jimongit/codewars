using System;
using System.Collections.Generic;
public class Kata
{
  public static int FindShort(string s)
  {
   string[] list = s.Split(' ');
   int minLen = list[0].Length;
   foreach (string str in list) minLen = Math.Min(minLen,str.Length);
   return minLen;
  }
 
}