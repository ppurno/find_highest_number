class HighestNumberFinder:
    def find_highest_number(self, numbers):
        max_Number = numbers[0]

        for item in numbers:
            if item > max_Number:
                max_Number = item

        return max_Number
