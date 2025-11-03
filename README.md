# Circular Dependency That pytest Cannot Detect

**Files: a.py ↔ b.py**

```
a.py imports b
b.py imports a
```

Both modules import each other, but they only access each other's attributes inside functions, not at module level.

**Result:** Python successfully imports both modules. The circular dependency exists but doesn't cause an error.

```bash
python -c "import a; import b"
python -c "import a; print(a.call_b())"
python -c "import b; print(b.call_a())"
```

All of these work fine. If you had pytest installed, `pytest a_test.py` and `pytest b_test.py` would also run successfully.

## Why It Works

Python can handle circular imports when:

- Modules use `import module` (not `from module import name`)
- Attributes are accessed inside functions (lazy), not at module level (eager)

The imports complete successfully because neither module tries to access the other's attributes during import time.
