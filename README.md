# flappy-bird-without-ml
Simple algorithm plays Flappy Bird to show that machine learning is not always necessary.

## Why should you care?

It seems that some people often try to apply machine learning to problems that have a much simpler
solution. Sometimes these solutions are tricky to find, which is one of the reasons why people choose
machine learning. But I think that if a simpler solution exists and can be discovered in less time
than it takes to train a machine learning model, then the simpler solution should be used instead.
So if you're designing a machine learning model, as you're thinking about the problem you're trying
to solve, you should be asking yourself at every step, "Can I solve this in a simpler way without
machine learning?"

A solution without machine learning will often take less computation time. And it's always ideal if
you can avoid having to train a model for hours or days. Furthermore, machine learning models are
difficult to debug because of how opaque they are. People cannot look at all the weight values in
a neural network, for instance, and truly understand the algorithm that the model is executing.

So to get readers to think about this, I chose to demonstrate a case where machine learning is often
used but unecessary. Enter Flappy Bird.

## What is Flappy Bird?

[Flappy Bird](https://flappybird.io/) is a game where you just press one button to avoid obstacles.
It's such as simple game that you'd think it should be easy. But no. It's incredibly difficult--and
addictive for some people--because it requires very precise timing.

## Why should you use Machine Learning?

People often use Flappy Bird as one of their first machine learning projects. And there's a good
reason why. When you're learning about machine learning, you want to start with simple problems
before working up to difficult problems. Flappy Bird is very simple. There's only one action
the player can make, and the game state can be described with very few parameters.

Even though I'm trying to convince you that machine learning on Flappy Bird is unecessary, I do
think it's a very good project to help students learn machine learning. But I think students need
to know that there's a better solution to Flappy Bird so that in the future--when they are machine
learning experts--they make sure to be selective about which problems they apply machine learning
to. A true expert should know which tool to use.


## Why should you NOT use Machine Learning?

One of the first steps in designing a model is to think about the minimum set of state parameters
you need to input ot your model to be able to come to a complete solution. After carefully
observing the mechanics of Flappy Bird I came up with a list of four parameters that would completely
describe the game state. But then I thought about whether any of these parameters were redundant
or irrelevant to solving the game. After combining the redundant parameters and removing the
irrelevant ones, I was left with only one parameter. With just one parameter in my mind, it was
easy for me to come up with a winning strategy, without even needing to think about machine learning.

The single state parameter I came up with was the vertical distance between the bird and the upper
edge of the approaching lower pipe. The winning strategy is this: If you're below the upper edge of
the approaching lower pipe, you jump. Otherwise, you jump as infrequently as possible to always
remain above this upper edge. It's a very simple strategy, and it works indefinitely.


## Running the game

You'll need to have python3 and pygame installed to run this project. Then you can just run:

```
$ python3 main.py
```

You'll see a very basic version of Flappy Bird. You can control the red "bird" (actually just a circle) with the space bar. The computer controls the orange bird.

See if you can make it further than the computer without dying! (hint: you can't)
