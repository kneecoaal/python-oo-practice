"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Create serial number with a start value (default: 100)."""
        self.start = start
        self.current = start 

    def generate(self):
        """Generate the next serial number and increment the counter."""
        serial_number = self.current
        self.current += 1
        return serial_number

    def reset(self):
        """Reset the serial number to the starting value."""
        self.current = self.start

