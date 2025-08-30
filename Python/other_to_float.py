import math


class Point:
    def __init__(self, x: float, y: float):
        """
        Initializes a Point in 2D space.

        Args:
            x (float): x-coordinate
            y (float): y-coordinate
        """
        self.x = x
        self.y = y

    def distance(self, other: 'Point') -> float:
        """
        Calculates the Euclidean distance between this point and another point.

        The calculation is based on the Pythagorean theorem, where:
        - dx is the horizontal difference (base of the triangle)
        - dy is the vertical difference (height of the triangle)
        - The distance is the hypotenuse:

        Formula:
            d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

        Args:
            other (Point): Another point in 2D space

        Returns:
            float: The distance between the two points
        """
        # Difference in x and y (horizontal and vertical sides of the triangle)
        dx = other.x - self.x
        dy = other.y - self.y

        # Applying the Pythagorean theorem
        distance = math.sqrt(dx ** 2 + dy ** 2)

        return distance


# ==============================
# Example usage
# ==============================

# Create two points
point1 = Point(0, 0)
point2 = Point(3, 4)

# Calculate the distance between them
result = point1.distance(point2)

# Print the result
print("Distance between point1 and point2:")
print(result)  # Expected output: 5.0
