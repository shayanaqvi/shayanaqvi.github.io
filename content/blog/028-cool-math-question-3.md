+++
title = 'Cool Math Question III'
date = 2024-08-20T17:02:34+05:00
Categories = ["Math"]
math = true
+++

Here's the question:

> |$x$     |$g(x)$  |
> |--------|--------|
> |-27     |3       | 
> |-9      |0       | 
> |21      |5       | 
> 
> The table shows three values of $x$ and their corresponding values of $g(x)$, where $g(x) = \frac{f(x)}{x+3}$ and $f$ is a linear function. What is the y-intercept of the graph $y=f(x)$ in the $xy$-plane?

This looks a lot more complicated than it actually is.

If

$$ g(x)=\frac{f(x)}{x+3} $$

then

$$ f(x) = g(x) \times (x+3) $$

Moreover, we know that $f(x)$ is linear, so if we were to theoretically input the values of the $x$s given, we could work out a gradient! From there, we could form an equation and solve for the y-intercept.

If we let $x=-27$, then $f(-27)=g(-27) \times (-27+3)$. This would simplify to $-72$. We now have one point that lies on $f(x)$. I'll pick $x=-9$ as my second point, since $f(x)$ will come to $0$.

Our two points are:

$$(-27, -72)$$

$$ (-9, 0) $$

The gradient from these two points comes to $4$. So,

$$f(x)=4x+C$$

Solving for C, we have:

$$C=f(x)-4x$$

We can input any of our coorindates here and get a value for C. I used the first set of coordinates, and this gave me $C=36$.

The y-intercept is thus $(0, 36)$.
