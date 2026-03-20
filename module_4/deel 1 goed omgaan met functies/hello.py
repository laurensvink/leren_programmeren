def towns_string(n):
    return "\n".join(f"Hello from function town {i}!" for i in range(1, n+1))

# Example usage:
result = towns_string(5)
print(result)