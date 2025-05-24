using System;

class Program
{
    static void Main()
    {
        // Get grade percentage from user
        Console.Write("Enter your grade percentage: ");
        string input = Console.ReadLine();
        int gradePercentage = int.Parse(input);

        string letter = "";  // Will hold the letter grade
        string sign = "";    // Will hold the + or - sign

        // Determine letter grade
        if (gradePercentage >= 90)
        {
            letter = "A";
        }
        else if (gradePercentage >= 80)
        {
            letter = "B";
        }
        else if (gradePercentage >= 70)
        {
            letter = "C";
        }
        else if (gradePercentage >= 60)
        {
            letter = "D";
        }
        else
        {
            letter = "F";
        }

        // Determine sign (only for grades A-D)
        if (letter != "F")
        {
            int lastDigit = gradePercentage % 10;
            
            if (lastDigit >= 7 && letter != "A")  // No A+
            {
                sign = "+";
            }
            else if (lastDigit < 3 && letter != "F")  // No F-
            {
                sign = "-";
            }
        }

        // Print the letter grade with sign
        Console.WriteLine($"Your letter grade is: {letter}{sign}");

        // Determine if student passed
        if (gradePercentage >= 70)
        {
            Console.WriteLine("Congratulations! You passed the course.");
        }
        else
        {
            Console.WriteLine("Keep working hard for next time!");
        }
    }
}