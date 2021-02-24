# study_cs61a
存放一些自己学习的文件
2021-2-23
  记录一下卡到我的东西
  1 Project 1: The Game of Hog 中的play功能时，脑子秀逗忘记了if和else只会执行其中一个.使用while循环和改变player=0 还是 1来实现切换对手
  2 higher-order function 参数可以是一个函数、返回的也是一个函数。
     
     def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,goal=GOAL_SCORE, say=silence):
        num_rolls=strategy0(score0,score1)
         ...
        return 
    def always_roll(n):
        def strategy(score, opponent_score):
          return n
    return strategy
    这个时候执行一个 play(always_roll(5), .....)时，strategy0实际上指向了strategy函数，所以strategy0(score0,score1)是可行的
2021-2-24
  1 Lab 2: Higher Order Functions中的Q5: Lambda the Environment Diagram
  >>> a = lambda x: x * 2 + 1
  >>> def b(b, x):
  ...     return b(x + a(x))
  >>> x = 3
  >>> b(a, x)
  ______
  这个问题一开始也想了半天，一直把return b(x + a(x))中的b想成重新调用了一次b函数。之后想了下b(a, x)中的a只是指向了这个lanmbda函数还没调用，所以里面那个return b(x + a(x))
  到最后其实是a(x+a(x))
