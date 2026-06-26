class Sample:
    x = 10  # Class variable (shared by all instances)

    @classmethod
    def modify(cls):
        cls.x += 1  # Modifies the shared class variable

s1 = Sample()
s2 = Sample()

# Call modify via the class or an instance
s1.modify()

print("s1.x:", s1.x)  # Output: 11
print("s2.x:", s2.x)  # Output: 11 (Changed for s2 as well!)