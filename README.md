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

## Why Are Circular Dependencies Bad?

1. **Makes code harder to understand** -- When module A depends on B and B depends on A, you can't fully understand either module in isolation. You must mentally load both modules simultaneously.

2. **Prevents independent testing** -- You can't test module A without also bringing in module B, and vice versa. This defeats the purpose of unit testing.

3. **Complicates refactoring and maintenance** -- Changing one module might break the other in unexpected ways. You can't extract or move one module without dealing with the other.

4. **Makes the codebase fragile** -- Changes ripple between modules unpredictably. You think you're making a small local change, but suddenly tests break in completely unrelated parts of the codebase because of hidden circular dependencies.

5. **Prevents clean module boundaries** -- Good architecture has clear dependency hierarchies (A→B→C). Circular dependencies mean there's no clear "lower level" vs "higher level".

6. **Can cause initialization issues** -- Python tolerates some circular imports, but they can fail in subtle ways. Module initialization order becomes non-deterministic, attributes might not be available when you expect them, and the failures can be intermittent depending on which module gets imported first.

7. **Hinders code reuse** -- You can't reuse module A in another project without also bringing module B. They're now a coupled pair, not independent components.

The real danger is that pytest doesn't catch circular dependencies, so teams can accumulate them without realizing it, until the codebase becomes a tangled mess where everything depends on everything else. This is why tools like Bazel that enforce stricter dependency rules can be valuable for large projects.
