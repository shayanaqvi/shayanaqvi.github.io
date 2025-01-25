+++
title = 'Integrating Inverse Tan'
date = 2023-12-30T19:23:02+05:00
Categories = ["Math"]
math = true
+++

We're going to do some integration by parts!

The thing to realize is that *you can integrate singular terms by parts*. $tan^{-1}(x)$ is indeed a singular term, however it is the same thing as $tan^{-1}(x) \times 1$. There's nothing to stop us from integrating that expression by parts.

Let's get started.

$$tan^{-1}(x) \times 1$$

For our purposes, we'll integrate 1 and derive $tan^{-1}(x)$. It may sound a bit stupid, but we can't integrate $tan^{-1}(x)$ at this moment since that's the whole point of this exercise! Anyways,

The integral of 1 with respect to $x$ is just $x$.

$$ tan^{-1}x \times \int(1)dx - \int(\frac{d}{dx}tan^{-1}(x) \times \int(1)dx) $$

If this looks a bit crazy, try working the expression out yourself. It isn't as bad as it looks.

Now, the derivative of $tan^{-1}(x)$ is $\frac{1}{1+x^2}$ (take this as a given for this purpose):

$$ tan^{-1}(x) \times x - \int(\frac{1}{1+x^2} \times x)dx $$

$$ xtan^{-1}(x) - \int(\frac{x}{1+x^2})dx $$

From here, there are two routes we can go down. We could

1. make a substitution
2. use the $\frac{f'(x)}{f(x)}$ property

It might sound a bit redundant, but you'll need to be familiar with the $\frac{f'(x)}{f(x)}$ property for both of these methods.

We'll go through both of them, starting with a substitution.

# Substitution

Let's define $u$ as $u=1+x^2$. Hence,

$$ du = 2x dx $$

$$ dx = \frac{du}{2x} $$

Now that we have $u$ and $dx$, let's plug these values in:

$$ xtan^{-1}(x) - \int(\frac{x}{u} \times \frac{du}{2x}) $$

>*To clarify, we went from:*
>
>$$ xtan^{-1}(x) - \int(\frac{x}{1+x^2})dx $$
>
>*to*
>
>$$ xtan^{-1}(x) - \int(\frac{x}{u} \times \frac{du}{2x}) $$
>
>*by means of a substitution.*

Let's look at $\frac{x}{u} \times \frac{du}{x}$: we can rewrite it as $\frac{x}{2ux}du$. We can DESTROY and ANNIHILATE the $x$ in this fraction.

$$ xtan^{-1}(x) - \int(\frac{1}{2u})du $$

$$ xtan^{-1}(x) - \frac{1}{2} \int(\frac{1}{u})du $$

Using the $\frac{f'(x)}{f(x)}$ property, we know that $\frac{1}{u}du$ will integrate to $ln(u)$. Hence:

$$ xtan^{-1}(x) - \frac{1}{2}[ln(u)] $$

And since $u=1+x^2$

$$ xtan^{-1}(x) - \frac{1}{2}ln(1+x^2) $$

That's it!

# Using $\frac{f'(x)}{f(x)}$

PLEASE make sure you're familiar with this property before continuing!

Here's where we currently stand:

$$ xtan^{-1} - \int(\frac{x}{1+x^2})dx $$

Focus on $\frac{x}{1+x^2}$.

We know that the derivative of the denominator of this fraction ($1+x^2$) with respect to $x$ is $2x$. It's a bit hard for me to put this into words, but using the $\frac{f'(x)}{f(x)}$ property, we can "morph" this $2x$ into the numerator of the fraction if we multiply it by $\frac{1}{2}$.

So, if we integrate $\frac{x}{1+x^2}$ like this, we'll end up with $\frac{1}{2}ln(1+x^2)$ by means of the $\frac{f'(x)}{f(x)}$ property. If we plug this into the rest of our expression, we'll end up with

$$ xtan^{-1}(x) - \frac{1}{2}ln(1+x^2) $$

That was *a lot faster*, but I only used this method for exam purposes. Weird as it may sound, I found the substitution more fun to do.

