**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Draw with Mouse

**Primary Actor**: User

**Goal in Context**: To draw on the canvas using the mouse as if it were a pencil on paper.

**Preconditions**: The program must be running and in a responsive state.

**Trigger**: User interacts with the canvas using the mouse.

**Scenario**:

1. User moves the mouse pointer over the canvas.
2. When the user presses and holds the left mouse button, the program detects the event.
3. The program changes the color of the pixel under the mouse pointer to the currently selected drawing color.
4. User can drag the mouse to draw lines or shapes on the canvas.
5. When the user releases the left mouse button, the drawing action stops.

**Exceptions**: If the program encounters an internal error, it displays an error message and allows the user to retry or exit.

**Priority**: High-priority

**When available**: First release

**Channel to actor**: The primary actor communicates through the program's user interface and the mouse.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: None

<hr>

(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
