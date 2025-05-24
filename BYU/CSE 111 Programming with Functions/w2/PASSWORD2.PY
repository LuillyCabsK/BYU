# Password Strength Checker


# ==============
# Initial Setup
# ==============

# Character type definitions
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"]

# ================
# Helper Functions
# ================

def word_in_file(word, filename, case_sensitive=False):
    """
    Check if a word exists in a file
    Args:
        word: Word to search for
        filename: File to search in
        case_sensitive: Whether to match case (default False)
    Returns:
        True if word is found, False otherwise
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                file_word = line.strip()
                if case_sensitive:
                    if file_word == word:
                        return True
                else:
                    if file_word.lower() == word.lower():
                        return True
    except FileNotFoundError:
        print(f"Warning: Could not find file {filename}")
    return False

def has_character_type(word, char_list):
    """
    Check if word contains any character from char_list
    Args:
        word: Word to check
        char_list: List of characters to look for
    Returns:
        True if any character is found, False otherwise
    """
    for char in word:
        if char in char_list:
            return True
    return False

def calculate_complexity(password):
    """
    Calculate password complexity score (0-4)
    Args:
        password: Password to evaluate
    Returns:
        Complexity score (1 point per character type used)
    """
    score = 0
    if has_character_type(password, LOWER):
        score += 1
    if has_character_type(password, UPPER):
        score += 1
    if has_character_type(password, DIGITS):
        score += 1
    if has_character_type(password, SPECIAL):
        score += 1
    return score

# =====================
# Password Evaluation
# =====================

def check_password_strength(password, min_length=10, strong_length=16):
    """
    Evaluate password strength and provide feedback
    Args:
        password: Password to check
        min_length: Minimum required length (default 10)
        strong_length: Length considered strong (default 16)
    Returns:
        Strength score (0-5)
    """
    # Check against dictionary words
    if word_in_file(password, "wordlist.txt"):
        print("\n⚠️ Password is a dictionary word - very insecure!")
        return 0
    
    # Check against common passwords
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("\n⚠️ Password is too common - not secure!")
        return 0
    
    # Check minimum length
    if len(password) < min_length:
        print(f"\n⚠️ Too short! Needs at least {min_length} characters")
        return 1
    
    # Check if length makes it strong
    if len(password) >= strong_length:
        print("\n✅ Excellent! Length makes this password strong")
        return 5
    
    # Calculate complexity-based strength
    complexity = calculate_complexity(password)
    strength = 1 + complexity
    
    # Provide improvement tips
    tips = []
    if not has_character_type(password, UPPER):
        tips.append("uppercase letters")
    if not has_character_type(password, DIGITS):
        tips.append("numbers")
    if not has_character_type(password, SPECIAL):
        tips.append("special characters")
    
    if tips:
        print(f"\n💡 Tip: Add {' or '.join(tips)} to strengthen")
    
    # Show visual rating
    print(f"\n🔐 Strength: {'★' * strength}{'☆' * (5 - strength)} ({strength}/5)")
    
    return strength

# ================
# User Interface
# ================

def show_welcome():
    """Display welcome message"""
    print("""
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║
    ██║     ██║  ██║███████║███████║╚███╔███╔╝
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ 
    """)
    print("Password Strength Checker")
    print("Check how strong your passwords are")
    print("Type 'quit' to exit\n")

def main():
    """Main program loop"""
    show_welcome()
    
    while True:
        password = input("Enter password: ").strip()
        
        # Exit condition
        if password.lower() in ['quit', 'q', 'exit']:
            print("\nGoodbye! Stay secure! 🔒")
            break
        
        # Validate input
        if not password:
            print("Please enter a password or 'quit' to exit")
            continue
        
        # Evaluate password
        score = check_password_strength(password)
        
        # Additional feedback
        if score <= 1:
            print("🚨 This password is very weak!")
        elif score <= 3:
            print("⚠️  This password could be stronger")
        elif score == 4:
            print("👍 Good password!")
        else:
            print("🎉 Excellent password!")
        
        print("-" * 40)  # Visual separator

# =============
# Program Start
# =============
if __name__ == "__main__":
    main()