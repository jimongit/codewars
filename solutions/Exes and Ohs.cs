using System.Linq;
using System;
public static class Kata 
{
  public static bool XO (string input)
  {
    if(input==null) return false;
    int Exes = 0; int Ohs=0;
    char[] chars = input.ToCharArray();
    foreach(Char c in chars)
    {
    if(Char.ToLower(c) == 'x') Exes++;
    if(Char.ToLower(c) == 'o') Ohs++;
    }
    return Exes==Ohs;
  }
}