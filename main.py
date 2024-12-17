from carbon_calculator import CarbonCalculator
from report_generator import ReportGenerator

def main():
    print("Welcome to the Carbon Footprint Monitoring Tool!")
    print("Let's help you understand and reduce your carbon footprint.\n")
    
    # Gather user inputs
    try:
        electricity_bill = float(input("Enter your average monthly electricity bill in euros: "))
        gas_bill = float(input("Enter your average monthly natural gas bill in euros: "))
        fuel_bill = float(input("Enter your average monthly fuel bill for transportation in euros: "))
        waste_generated = float(input("Enter the amount of waste you generate per month in kilograms: "))
        recycling_percentage = float(input("Enter the percentage of waste recycled or composted: ")) / 100
        kilometers_traveled = float(input("Enter the total kilometers traveled per year for business purposes: "))
        fuel_efficiency = float(input("Enter the average fuel efficiency of the vehicles used in liters per 100 kilometers: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    # Calculate carbon footprint
    calculator = CarbonCalculator(
        electricity_bill, gas_bill, fuel_bill, 
        waste_generated, recycling_percentage, 
        kilometers_traveled, fuel_efficiency
    )
    total_emissions = calculator.calculate_total_emissions()
    
    # Generate and display the report
    report = ReportGenerator(total_emissions)
    report.generate()

if __name__ == "__main__":
    main()