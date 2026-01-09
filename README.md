## Problem Brief

The pytest.raises() helper validates that a specific exception type
is raised. Currently, passing a non-exception input results in
unclear error messaging.

### Expected Behavior

- A TypeError must be raised if the provided argument is not
  an exception type.
- The error message must include the invalid input's type name.
- Existing behavior for valid exception types must remain unchanged.
- No unrelated functionality should be affected.

This behavior must be deterministic and fully testable.
