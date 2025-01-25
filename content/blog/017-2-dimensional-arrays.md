+++
title = '2-Dimensional Arrays'
date = 2024-05-19T20:17:50+05:00
Categories = ["Computers", "Programming"]
+++

All explanations I’ve heard from teachers AND from the few textbooks I’ve read have such a convoluted explanation of this data structure.

To put it simply, a 2-Dimensional array is nothing more than a single array that contains multiple other arrays. That’s it!

{{< highlight python "linenos=inline, style=arduino" >}}
array_2d = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
{{< /highlight >}}

When you arrange it like this, you see the tabular structure everyone talks about.

The other thing to know is how to loop through such an array. You’ll need exactly 2 loops for this. One loop to select each array in `array_2d`; the other to go through the items in each array of `array_2d`.

Think of it this way: when you loop through a regular ol' array, you loop through each individual element, right?

{{< highlight python "linenos=inline, style=arduino" >}}
array = [1, 2, 3, 4, 5]
for item in array:
  print(array)
{{< /highlight >}}

Now, if we let:

{{< highlight python "linenos=inline, style=arduino" >}}
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
{{< /highlight >}}

and we also let:

{{< highlight python "linenos=inline, style=arduino" >}}
array_2d = [a, b, c]
{{< /highlight >}}

then looping through a 2-dimensional array is no different.

At any given moment, our loop variable will hold `a`, `b`, or `c`, as shown below:

{{< highlight python "linenos=inline, style=arduino" >}}
for array in array_2d:
  print(array) # this will print the entirety of a, b, and c.
{{< /highlight >}}

It is at this moment you require a second loop if you want to access each element in `a`, `b`, or `c`.

{{< highlight python "linenos=inline, style=arduino" >}}
array_2d = [a, b, c]

for array in array_2d: # loop through the 2-dimensional array
  for item in array: # loop through each item in the currently selected array
    print(item)
{{< /highlight >}}
