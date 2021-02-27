# study_cs61a
存放一些自己学习的文件，记录一下卡到我的东西  
#### 2021-2-23  
  1. Project 1: The Game of Hog 中的play功能时，脑子秀逗忘记了if和else只会执行其中一个.使用while循环和改变player=0 还是 1来实现切换对手  
  2. higher-order function 参数可以是一个函数、返回的也是一个函数。  
  ```
    def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,goal=GOAL_SCORE, say=silence):
      num_rolls=strategy0(score0,score1)
      ...
      return 
    def always_roll(n):
      def strategy(score, opponent_score):
        return n
    return strategy
  ```
   这个时候执行一个 play(always_roll(5), .....)时，strategy0实际上指向了strategy函数，所以strategy0(score0,score1)是可行的  
#### 2021-2-24  
  1. Lab 2: Higher Order Functions中的Q5: Lambda the Environment Diagram    
  ```
    a = lambda x: x * 2 + 1
    def b(b, x):
      return b(x + a(x))
    x = 3
    b(a, x)
    ______
  ```  
  这个问题一开始也想了半天，一直把return b(x + a(x))中的b想成重新调用了一次b函数。之后想了下b(a, x)中的a只是指向了这个lanmbda函数还没调用，所以里面那个return b(x + a(x))
  到最后其实是a(x+a(x))  
#### 2021-2-27  
  1. hog项目的Problem 8，这题目主要还是难在没理解英文意思，一开始以为只是简单把函数作为参数传进执行X次算出平均值，后来发现敲代码前的test题目里有一个  
 ```
    from hog import *
    dice = make_test_dice(3, 1, 5, 6)
    averaged_roll_dice = make_averaged(roll_dice, 1000)
    averaged_roll_dice(2, dice)
  ```
  这最后居然执行的时候还能继续传参，卡了我一会，知道要用args,但是直到代码都通了还是没正确翻译出这个题目啥意思。原题如下
  Problem 8 (2 pt)
Implement the make_averaged function, which is a higher-order function that takes a function fn as an argument. It returns another function that takes the same number of arguments as fn (the function originally passed into make_averaged). This returned function differs from the input function in that it returns the average value of repeatedly calling fn on the same arguments. This function should call fn a total of num_samples times and return the average of the results.

To implement this function, you need a new piece of Python syntax! You must write a function that accepts an arbitrary number of arguments, then calls another function using exactly those arguments. Here's how it works.

Instead of listing formal parameters for a function, we write *args. To call another function using exactly those arguments, we call it again with *args. 
