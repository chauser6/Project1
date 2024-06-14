recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,    ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}
class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("How many large dollars ($1)? "))
        half_dollars = int(input("How many half dollars ($0.5)? "))
        quarters = int(input("How many quarters ($0.25)? "))
        nickels = int(input("How many nickels ($0.05)? "))

        total = (large_dollars * 1) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
        return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")


    def report_resources(self):
        """Print the current resources."""
        print("Current resources:")
        for item, amount in self.machine_resources.items():
            print(f"{item}: {amount}")


    def ham_sandwich_maker(self):
        """Main function to run the ham sandwich maker program."""
        while True:
            choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

            if choice == "off":
                print("Turning off the machine. Goodbye!")
                break

            elif choice == "report":
                self.report_resources()

            elif choice in ["small", "medium", "large"]:
                sandwich_recipe = recipes[choice]
                if not self.check_resources(sandwich_recipe["ingredients"]):
                    continue

                cost = sandwich_recipe["cost"]
                print(f"The cost of a {choice} sandwich is ${cost:.2f}.")
                total_inserted = self.process_coins()

                if self.transaction_result(total_inserted, cost):
                    self.make_sandwich(choice, sandwich_recipe["ingredients"])

            else:
                print("Invalid choice. Please select again.")
# Create an instance of SandwichMachine
machine = SandwichMachine(resources)

# Run the ham sandwich maker program
machine.ham_sandwich_maker()
