# credit_card_geimport random
import sys
from datetime import datetime

class CreditCardGenerator:
    def __init__(self):
        self.card_types = {
            'visa': {'prefixes': ['4'], 'lengths': [13, 16]},
            'mastercard': {'prefixes': ['51', '52', '53', '54', '55', '2221', '2720'], 'lengths': [16]},
            'amex': {'prefixes': ['34', '37'], 'lengths': [15]},
            'discover': {'prefixes': ['6011', '65'], 'lengths': [16]},
        }
    
    def generate(self, card_type=None, count=1):
        """Generate valid credit card numbers"""
        if card_type and card_type.lower() not in self.card_types:
            raise ValueError(f"Unsupported card type. Available: {', '.join(self.card_types.keys())}")
        
        results = []
        for _ in range(count):
            if card_type:
                card_info = self.card_types[card_type.lower()]
                prefix = random.choice(card_info['prefixes'])
                length = random.choice(card_info['lengths'])
            else:
                # Random card type
                card_type = random.choice(list(self.card_types.keys()))
                card_info = self.card_types[card_type]
                prefix = random.choice(card_info['prefixes'])
                length = random.choice(card_info['lengths'])
            
            # Generate the base number with the prefix
            number = prefix
            number += ''.join([str(random.randint(0, 9)) for _ in range(length - len(prefix) - 1)])
            
            # Calculate and append check digit using Luhn algorithm
            check_digit = self._calculate_luhn_check_digit(number)
            number += str(check_digit)
            
            # Format with spaces for readability
            formatted_number = ' '.join([number[i:i+4] for i in range(0, len(number), 4)])
            results.append((card_type.upper(), formatted_number))
        
        return results
    
    def _calculate_luhn_check_digit(self, number):
        """Calculate the check digit using Luhn algorithm"""
        total = 0
        reverse_digits = number[::-1]
        
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        
        return (10 - (total % 10)) % 10
    
    def validate(self, number):
        """Validate a credit card number using Luhn algorithm"""
        # Remove any non-digit characters
        number = ''.join(filter(str.isdigit, number))
        
        if not number:
            return False
        
        # Calculate check digit
        check_digit = self._calculate_luhn_check_digit(number[:-1])
        return check_digit == int(number[-1])
    
    def print_results(self, results):
        """Display the generated card numbers"""
        print("\nGenerated Credit Card Numbers:")
        print("-" * 50)
        for i, (card_type, number) in enumerate(results, 1):
            print(f"{i}. {card_type}: {number}")
        print("\nNote: These numbers are generated for testing and educational purposes only.")
        print("They are not real credit card numbers and cannot be used for actual transactions.")

def main():
    generator = CreditCardGenerator()
    
    print("Credit Card Number Generator")
    print("=" * 50)
    print("Available card types: VISA, MasterCard, American Express, Discover")
    print("Or leave blank for random card types")
    
    try:
        card_type = input("\nEnter card type (blank for random): ").strip()
        if card_type and card_type.lower() not in generator.card_types:
            print(f"Error: Unsupported card type. Available: {', '.join(generator.card_types.keys())}")
            return
        
        count_input = input("How many cards to generate? (default 1): ").strip()
        count = int(count_input) if count_input.isdigit() and int(count_input) > 0 else 1
        
        results = generator.generate(card_type if card_type else None, count)
        generator.print_results(results)
        
        # Option to save to file
        save = input("\nSave to file? (y/N): ").strip().lower()
        if save == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"credit_cards_{timestamp}.txt"
            with open(filename, 'w') as f:
                f.write("Generated Credit Card Numbers\n")
                f.write("=" * 50 + "\n")
                for i, (card_type, number) in enumerate(results, 1):
                    f.write(f"{i}. {card_type}: {number}\n")
                f.write("\nNote: These numbers are generated for testing and educational purposes only.\n")
                f.write("They are not real credit card numbers and cannot be used for actual transactions.\n")
            print(f"Results saved to {filename}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()nerator
