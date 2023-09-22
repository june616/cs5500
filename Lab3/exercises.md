# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
   - MObject is a concrete class. In the given code, the MObject class doesn't have any abstract methods and can be instantiated directly, making it a concrete class.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
   - The del method is a special method in Python known as a destructor. If it were implemented, it would be called when an instance of the class is about to be destroyed.
1. What class does Texture inherit from?
   - The Texture class inherits from the Image class.
1. What methods and attributes does the Texture class inherit from 'Image'?
   - The Texture class inherits all the methods and attributes of the Image class since it doesn't override or add any methods or attributes of its own. These methods include init, getWidth, getHeight, getPixelColorR, getPixels, and setPixelsToRandomValue. It also inherits attributes like m_width, m_height, m_colorChannels, and m_Pixels.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
   - I believe that a Texture should have a 'has-a' (composition) relationship with Image because a texture is not strictly an image, but rather a representation that contains an image. An 'Image' class encapsulates the characteristics of a digital image, while a 'Texture' may have additional attributes or methods specific to how it is applied or rendered on a surface. Here is the refactored Texture code:
   ```
   class Texture:
    	def __init__(self, w, h):
        	self.image = Image(w, h)
   ```
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us?
   - Yes, Python automatically creates default constructors if they aren't explicitly defined in the class.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:

- The first time the logger is constructed, it will print out:
  - `Logger created exactly once`
- If the logger is already initialized, it will print: - `logger already created`
  Note: You do not 'have' a constructor, but you construct the object in the _instance_ member function where you will create an object.  
  Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

Singletons in Python are not inherently thread-safe. Multiple threads can still attempt to create an instance at the same time, leading to race conditions. This means that if multiple threads try to create an instance at the same time, they might end up creating multiple instances, violating the singleton principle.
