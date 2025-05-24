using System;
class Program
{
    static void Main()
    {
        string name;
        int age;
        // Input
        onsole.WriteLine("Welcome to C#");
        Console.WriteLine("Enter your name:");
        name = console.ReadLine();
        Console.Write("Enter your age: ");
        age = Convert.ToInt32(Console.ReadLine());

        // Output
        Console.WriteLine($"Hello {name}! You are {age} years old. ");
    }
}
