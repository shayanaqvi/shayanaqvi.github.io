+++
title = 'Cool Math Question II'
date = 2024-07-26T16:47:34+05:00
Categories = ["Math"]
math = true
+++

> $$f(x) = ax^2 = 4x + c$$
> In the given quadratic function, $a$ and $c$ are constants. The graph of $y=f(x)$ in the $xy$- plane is a parabola that opens upward and has a vetex at the point $(h, k)$, where $h$ and $k$ are constants. If $k<0$ and $f(-9) = f(3)$, which of the following must be true?
>
> 1. $c \gt 0$
> 2. $a \geq 1$

Let's start off with this piece of information: $$f(-9)=f(3)$$

Note that:

$$ f(-9) = 81a-36 + c $$

and

$$ f(3)=9a+12+c $$

We can equate both of these and solve for $a$.

$$ 81a-36+c=9a+12+c $$

We can DESTROY the $c$ on both sides.

$$ 81a-36=9a+12 $$

Solving for $a$, we get $a=\frac{2}{3}$.

We've found that condition 2 is false.

Now, we will simplify our expression for $f(x)$ by replacing the $a$ with $\frac{2}{3}$.

$$ f(x) = \frac{2}{3}x^2+4x+c $$

We are also given the coordinates of the vertex of this parabola: $(h, k)$. If we were to complete the square on our brand new $f(x)$, we may be able to obtain $h$ or $k$ (since you can read off the coordinates of the vertex of a quadratic in completed-square form).

We'll do just that; we end up with:

$$ f(x) = \frac{2}{3}(x+3)^2-6+c $$

Since we have some extra information about $k$ ($k \lt 0$), we can equate it to $-6+c$.

$$ -6+c = k$$

Solving this, we find $c=k+6$. How does this help?

Let's test this two ways. We'll asign $k$ any two values less than zero (remember $k \lt 0$): I'll choose $-2$ and $-10$. If we plug either value into our equation in $c$, we can see if the first condition holds.

For $k=-2$, $c$ comes to $+4$. However, for $k=-10$, $c$ comes to $-4$. Thus, condition 1 isn't *always* true.

We can conclude that both of the conditions are false. 
