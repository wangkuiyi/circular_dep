# pytest Cannot Detect Circular Dependency even if Test Coverage Rate is 100%

This is one of the reason that if you manage a large Python project, you'd like other tools, like, Bazel and bazel test.

In this project, we have two files:

https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/a.py#L1-L9

and

https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/b.py#L1-L9

Each one of them provides a function and calls the function provided by the other -- this is a circular dependency.

The authors of this project pursue high test coverage and wrote tests for each of these modules and made sure that the coverage is 100%.

https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/a_test.py#L1-L9

and

https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/b_test.py#L1-L9

Both `pytest a_test.py` and `pytest b_test.py` would run successfully -- without error on the circular dependency

```
17:58 $ pytest a_test.py 
============================================================================= test session starts =============================================================================
platform darwin -- Python 3.10.12, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/y/w/circular_dep
plugins: xdist-3.8.0, timeout-2.4.0, asyncio-0.21.1, anyio-4.10.0
asyncio: mode=strict
collected 2 items                                                                                                                                                             

a_test.py ..                                                                                                                                                            [100%]

============================================================================== 2 passed in 0.01s ==============================================================================

17:59 $ pytest b_test.py 
============================================================================= test session starts =============================================================================
platform darwin -- Python 3.10.12, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/y/w/circular_dep
plugins: xdist-3.8.0, timeout-2.4.0, asyncio-0.21.1, anyio-4.10.0
asyncio: mode=strict
collected 2 items                                                                                                                                                             

b_test.py ..                                                                                                                                                            [100%]

============================================================================== 2 passed in 0.01s ==============================================================================
```

It is out of the scope of this project to explain the terrible consequences of circular dependencis.
