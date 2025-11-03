# pytest Cannot Detect Circular Dependencies Even with 100% Test Coverage

This is one of the reasons why you might want to use additional tools like Bazel and bazel test when managing a large Python project.

In this project, we have two files:

<https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/a.py#L1-L9>

and

<https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/b.py#L1-L9>

Each module provides a function and calls the function from the other module -- this is a circular dependency.

The authors of this project pursue high test coverage and wrote tests for each module to ensure 100% coverage.

<https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/a_test.py#L1-L9>

and

<https://github.com/wangkuiyi/circular_dep/blob/952cb713a59a39c156ec2b3decfdde4715ae948b/b_test.py#L1-L9>

Both `pytest a_test.py` and `pytest b_test.py` run successfully without detecting the circular dependency

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

It is beyond the scope of this project to explain the consequences of circular dependencies.
