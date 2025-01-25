+++
title = 'Cool Math Question'
date = 2024-06-28T15:19:02+05:00
Categories = ["Math"]
math = true
+++

This is from the SAT. It gave me a bit of a pause but was fun to work through.

{{< image
  src="img/cool-math-question/cm.png"
  frame="true"
  caption="In the given figure, $BC$ is the diameter of the circle. If the length $BC$ is equal to $132$ and the length $AB$ is equal to $\sqrt{363}$, what is the value of $\frac{BC}{BD}$?"
>}}

The first thing to realise is that $\triangle ACB$ is a right angle triangle. If you have two chords intersecting at a point that lies on the cirumference of a circle, they meet at right angles.

The second this to realise is that if we can figure out the length of the line $AD$, we can use Pythagoras' to figure out the length of $BD$.

We can figure out the length of $AD$ if we can get $\angle ABC$. We'll use the sine of that angle.

And finally, we can get $\angle ABC$ through some regular ol' trigonometry. We know two sides of the right angle triangle $\triangle ABC$. For this, we'll get $\angle ACB$, which turns out to be $arcsin(\frac{\sqrt{363}}{132})$. Now, we'll subtract that value from $90$ to get $\angle ABC$. We'll keep this value exact; it's $90-arcsin(\frac{\sqrt{363}}{132})$.

We'll plonk this angle into an equation with sine: 

$$sin(90-arcsin(\frac{\sqrt{363}}{132})) = \frac{AD}{\sqrt{363}}$$ 

Solve for $AD$ and you get about $18.85$, but we won't round off yet. We'll call this value "$A$".

Now, we'll use Pythagoras' to solve for BD. $\sqrt{(\sqrt{363})^2-A^2}$ comes to exactly $\frac{11}{4}$. This is the length of BD.

Hence, $\frac{BC}{BD}$ comes to $\frac{132}{\frac{11}{4}}$, which simplifies to $48$ exactly. Wow!

There are probably simpler approaches, but this worked for me.
