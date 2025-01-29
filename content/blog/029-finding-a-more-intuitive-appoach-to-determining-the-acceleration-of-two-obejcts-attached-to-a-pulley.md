+++
title = 'Finding a more intuitive appoach to determining the acceleration of two obejcts attached to a pulley'
date = 2024-09-03T17:17:46+05:00
Categories = ["Math"]
math = true
+++

The title is a bit of a mouthful, but I'll explain what we're trying to do here.

Consider the following:

> Two particles $A$ and $B$ have masses $0.35$ kg and $0.45$ kg respectively. The particles are attached to the ends of a light inextensible string which passes over a small fixed smooth pulley which is 1 metre above the horizontal ground. Initially particle $A$ is held at rest on the ground vertically below the pulley, with the string taut. Particle $B$ hangs vertically below the pulley at a height of $0.64$ m above the ground. Particle $A$ is released.
>
> Find the speed of $A$ at the instant $B$ reaches the ground.

I'm not going to solve the entire question but I'll go as far as forming equations for the acceleration of $A$ and $B$.

This is the situation:

{{< image
  frame="true"
  caption="Levitating pulley"
  src="img/intuitive-acceleration/diagram.jpg"
>}}

We know that for both $A$ and $B$, their acceleration is of the same magnitude, but opposite in direction. The tension ($T$) in the string (unknown) is the same for both. Typically, in such situations, where both $a$ and $T$ are unknown, you'd create two equations (in order to resolve the forces) and solve them simultaneously.

$$ \Sigma F_A = m_Aa = W_A-T $$
$$ \Sigma F_B = m_Ba = T-W_B $$

These are the two equations you'd generally see. Most explanations I've seen tend to either neglect or barely explain why the second equation is that way. Why, now, are we subtracting weight from tension instead of the other way round? Sure, these two equations are convenient to work with, but why are we doing that?

A nice way to look at this: we know that the *magnitude* of the acceleration is the same for both $A$ and $B$. In other words, $|a|$ is the same for both. To illustrate this, let's set up equations in terms of $|a|$:

$$ m_A|a| = W_A-T $$
$$ |a|=\frac{W_A-T}{m_A} $$

We'll do the same for B:

$$ m_B|a| = W_B-T $$
$$ |a|=\frac{W_B-T}{m_B} $$

We now have *4* equations in $a$ ("expand" the modulus, if you will):
1. $ a = \frac{W_A-T}{m_A} $

2. $ a = \frac{T-W_A}{m_A} $

3. $ a = \frac{W_B-T}{m_B} $

4. $ a = \frac{T-W_B}{m_B} $

All of these will yield the same *magnitude* of acceleration. You can pick any whichever of these are convenient and solve for whatever you need.


