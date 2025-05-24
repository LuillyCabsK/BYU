# Password Strength Checker
# This program checks the strength of passwords based on various criteria including:
# - Presence in dictionary files
# - Length requirements
# - Character complexity
#
# Enhancement: Added color to the output messages for better visibility and user experience

# Character type definitions
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"]

# ANSI color codes for enhanced output
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'RESET': '\033[0m'
}

def word_in_file(word, filename, case_sensitive=False):
    """Check if a word exists in a file (line by line)"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if line_word == word:
                        return True
                else:
                    if line_word.lower() == word.lower():
                        return True
    except FileNotFoundError:
        print(f"{COLORS['RED']}Error: File {filename} not found.{COLORS['RESET']}")
    return False

def word_has_character(word, character_list):
    """Check if any character in the word is in the character list"""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Calculate complexity based on character types present in the word"""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Evaluate password strength based on various criteria"""
    # Check if password is in dictionary (case insensitive)
    if word_in_file(password, "wordlist.txt"):
        print(f"{COLORS['RED']}'{password}' is a dictionary word and is not secure.{COLORS['RESET']}")
        return 0
    
    # Check if password is in top passwords list (case sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print(f"{COLORS['RED']}'{password}' is a commonly used password and is not secure.{COLORS['RESET']}")
        return 0
    
    # Check length requirements
    if len(password) < min_length:
        print(f"{COLORS['YELLOW']}'{password}' is too short and is not secure.{COLORS['RESET']}")
        return 1
    
    if len(password) >= strong_length:
        print(f"{COLORS['GREEN']}'{password}' is long, length trumps complexity - this is a good password.{COLORS['RESET']}")
        return 5
    
    # Calculate complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity
    
    # Provide feedback based on strength
    if strength == 2:
        print(f"{COLORS['YELLOW']}'{password}' has basic complexity. Consider adding more character types.{COLORS['RESET']}")
    elif strength == 3:
        print(f"{COLORS['BLUE']}'{password}' has moderate complexity.{COLORS['RESET']}")
    elif strength == 4:
        print(f"{COLORS['GREEN']}'{password}' has good complexity.{COLORS['RESET']}")
    elif strength == 5:
        print(f"{COLORS['GREEN']}'{password}' has excellent complexity!{COLORS['RESET']}")
    
    return strength

def main():
    """Main program loop"""
    print(f"{COLORS['BLUE']}Password Strength Checker{COLORS['RESET']}")
    print("Enter a password to check its strength (or 'q' to quit)")
    
    while True:
        password = input("\nEnter password: ").strip()
        
        if password.lower() == 'q':
            print("Goodbye!")
            break
        
        if not password:
            print(f"{COLORS['RED']}Error: Please enter a password.{COLORS['RESET']}")
            continue
        
        strength = password_strength(password)
        print(f"Password strength: {strength}/5")

if __name__ == "__main__":
    main()