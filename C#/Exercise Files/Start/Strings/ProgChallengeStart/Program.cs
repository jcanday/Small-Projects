using System;

namespace ProgChallengeStart
{
    class Program
    {
        static void Main(string[] args)
        {
            // Choose a random number between 0 and 20
            int theNumber = new Random().Next(20);

            // Print the game greeting and instructions
            Console.WriteLine("Let's Play 'Guess the Number'!");
            Console.WriteLine("I'm thinking of a number between 0 and 20.");
            Console.WriteLine("Enter your guess, or -1 to give up.");

            // Keep track of the number of guesses and the current user guess

            // Start the game and run until user quits or guesses correctly
            // HINT: You'll need a way to convert the user's input to an integer
            int guesses = 0;
            string inputGuess = "";
            int answer = 0;
            bool correct = false;
            while (inputGuess != "-1"){
                inputGuess = Console.ReadLine();
                try{
                    answer = int.Parse(inputGuess);
                } 
                catch {
                    Console.WriteLine("Enter a valid number!");
                }
                finally{
                    guesses ++;
                }
                if(answer == theNumber){
                    Console.WriteLine("Correct");
                    Console.WriteLine($"Number of guesses {guesses}");
                    break;
                }
                else if(answer > theNumber){
                    Console.WriteLine("Nope, lower than that");
                    Console.WriteLine("Whats your guess?");
                }
                else{
                    Console.WriteLine("Nope, higher than that");
                    Console.WriteLine("Whats your guess?");
                }
            }
                
        }
    }
}
