+++
title = 'Dealing with this integral once and for all'
date = 2024-09-21T17:43:43+05:00
Categories = ["Math"]
math = true
+++

The formula sheet Cambridge gives you during your exam tells you the following about this particular integral:

$$ \int \frac{1}{x^2+a^2}dx = \frac{1}{a}tan^{-1}(\frac{x}{a}) $$

This works for integrals of the form $\frac{1}{x^2+a}$ where $a$ is any rational number. You can still use this for integrals of the form $\frac{1}{bx^2+a}$, where $b$ is also a rational number; we just have to modify it a bit. What we're looking for, in essence, is for the coefficient of $x^2$ to be $1$.

We'll deal with $\frac{1}{4x^2+1}$ as an example.

$$ \int \frac{1}{4x^2+1}dx $$

Taking $4$ as common from the denominator:

$$ \int \frac{1}{4(x^2+\frac{1}{4})}dx $$

Now, we'll take the constant "outside":

$$ \frac{1}{4} \int \frac{1}{x^2+\frac{1}{4}} $$

We'll integrate as normal from here:

$$ \frac{1}{4} \times [ \frac{1}{\sqrt{\frac{1}{4}}}tan^{-1}(\frac{x}{\sqrt{\frac{1}{4}}}) ] $$

$$ \frac{1}{4} \times [ 2tan^{-1}(2x)] $$

And we'll end up with $\frac{1}{2}tan^{-1}(2x)$. Problem solved!
