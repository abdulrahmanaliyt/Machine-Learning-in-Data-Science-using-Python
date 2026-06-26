# understanding static methods
class Sample:
    # Class variable or static var to store the count of instances
    instance_count = 0

    # constructor that increments instance_count when an instances is created
    def __init__(self):        
        Sample.instance_count += 1

    # Static method to display the total no of instances
    @staticmethod
    def get_instance_count():
        return Sample.instance_count

# Creating instances 3 times
s1 = Sample()
s2 = Sample()
s3 = Sample()

# Accessing the count using the static method
print("Total instances created:", Sample.get_instance_count())