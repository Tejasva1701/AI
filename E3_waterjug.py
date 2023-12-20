# Write a program to implement Water Jug Problem

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount
        self.visited_states = set()
        self.path = []

    def is_valid_state(self, jug1_amount, jug2_amount):
        return (
            0 <= jug1_amount <= self.jug1_capacity
            and 0 <= jug2_amount <= self.jug2_capacity
        )

    def solve(self, jug1_amount, jug2_amount):
        if jug1_amount == self.target_amount and jug2_amount == 0:
            return True

        state = (jug1_amount, jug2_amount)

        if state in self.visited_states:
            return False

        self.visited_states.add(state)

        # Fill jug1 from the tap
        if jug1_amount < self.jug1_capacity:
            self.path.append(f"Fill {self.jug1_capacity}-liter jug")
            if self.solve(self.jug1_capacity, jug2_amount):
                return True
            self.path.pop()

        # Fill jug2 from the tap
        if jug2_amount < self.jug2_capacity:
            self.path.append(f"Fill {self.jug2_capacity}-liter jug")
            if self.solve(jug1_amount, self.jug2_capacity):
                return True
            self.path.pop()

        # Pour water from jug1 to jug2
        if jug1_amount > 0 and jug2_amount < self.jug2_capacity:
            pour_amount = min(jug1_amount, self.jug2_capacity - jug2_amount)
            self.path.append(
                f"Pour {pour_amount}-liters from {self.jug1_capacity}-liter jug to {self.jug2_capacity}-liter jug"
            )
            if self.solve(jug1_amount - pour_amount, jug2_amount + pour_amount):
                return True
            self.path.pop()

        # Pour water from jug2 to jug1
        if jug2_amount > 0 and jug1_amount < self.jug1_capacity:
            pour_amount = min(jug2_amount, self.jug1_capacity - jug1_amount)
            self.path.append(
                f"Pour {pour_amount}-liters from {self.jug2_capacity}-liter jug to {self.jug1_capacity}-liter jug"
            )
            if self.solve(jug1_amount + pour_amount, jug2_amount - pour_amount):
                return True
            self.path.pop()

        # Empty jug1
        if jug1_amount > 0:
            self.path.append(f"Empty {self.jug1_capacity}-liter jug")
            if self.solve(0, jug2_amount):
                return True
            self.path.pop()

        # Empty jug2
        if jug2_amount > 0:
            self.path.append(f"Empty {self.jug2_capacity}-liter jug")
            if self.solve(jug1_amount, 0):
                return True
            self.path.pop()

        return False

    def print_solution(self):
        if self.solve(0, 0):
            for step in self.path:
                print(step)
        else:
            print("No solution found.")

def main():
    jug1_capacity = 5
    jug2_capacity = 3
    target_amount = 2

    problem = WaterJugProblem(jug1_capacity, jug2_capacity, target_amount)
    problem.print_solution()

if __name__ == "__main__":
    main()


#Sample Output 
# Fill 5-liter jug
# Fill 3-liter jug
# Empty 5-liter jug
# Pour 3-liters from 3-liter jug to 5-liter jug
# Fill 3-liter jug
# Pour 2-liters from 3-liter jug to 5-liter jug
# Empty 5-liter jug
# Pour 1-liters from 3-liter jug to 5-liter jug
# Fill 3-liter jug
# Pour 3-liters from 3-liter jug to 5-liter jug
# Fill 3-liter jug
# Pour 1-liters from 3-liter jug to 5-liter jug
# Empty 5-liter jug
# Pour 2-liters from 3-liter jug to 5-liter jug