def invest(amount: float, rate: float, years: int):
    """Calculate and display investment growth over time."""
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def main():
    # Get user input
    principal = float(input("Enter the initial amount: "))
    rate = float(input("Enter the annual rate of return (as a decimal): "))
    years = int(input("Enter the number of years: "))
    
    # Call invest function
    invest(principal, rate, years)

if __name__ == "__main__":
    main()
