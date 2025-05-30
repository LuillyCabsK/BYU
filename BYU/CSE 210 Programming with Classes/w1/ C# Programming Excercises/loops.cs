using System;

class Program
{
    static void Main()
    {
        // Initialize random number generator
        Random randomGenerator = new Random();
        bool playAgain = true;
        
        while (playAgain)
        {
            // Generate random number between 1-100
            int magicNumber = randomGenerator.Next(1, 101);
            int guessCount = 0;
            int guess = 0;
            
            Console.WriteLine("Welcome to Guess My Number Game!");
            Console.WriteLine("I've picked a number between 1 and 100.");
            
            // Game loop
            while (guess != magicNumber)
            {
                Console.Write("What is your guess? ");
                string input = Console.ReadLine();
                
                // Validate input
                if (!int.TryParse(input, out guess))
                {
                    Console.WriteLine("Please enter a valid number.");
                    continue;
                }
                
                guessCount++;
                
                // Check guess against magic number
                if (guess < magicNumber)
                {
                    Console.WriteLine("Higher");
                }
                else if (guess > magicNumber)
                {
                    Console.WriteLine("Lower");
                }
                else
                {
                    Console.WriteLine($"You guessed it in {guessCount} tries!");
                }
            }
            
            // Ask if player wants to play again
            Console.Write("Would you like to play again? (yes/no) ");
            string response = Console.ReadLine().ToLower();
            playAgain = (response == "yes");
        }
        
        Console.WriteLine("Thanks for playing!");
    }
}