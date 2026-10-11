"""
  Write a function that determines a valid package installation order by resolving
  dependencies. Use topological sorting to ensure dependencies are installed before
  the packages that require them.
  
  The function should:
  - Take a dictionary where keys are package names and values are lists of dependencies
  - Return packages in installation order (dependencies first)
  - Return empty list if no valid order exists (circular dependencies)
  - Handle empty input and isolated dependency chains
  - Ignore references to packages not in the input dictionary
  
  Algorithm requirements:
  - Use topological sorting (e.g., Kahn's algorithm)
  - Process packages with no remaining dependencies first
  - Ensure deterministic output when multiple valid orders exist
  
  Edge cases to handle:
  - Empty input: return empty list
  - Packages with no dependencies: include in output first
  - Multiple independent chains: process all chains
  - Circular dependencies: return empty list
  - Non-existent dependencies: ignore missing packages
  - Self-dependencies: return empty list
  
  Notes:
  - For deterministic output, process packages alphabetically when choices exist
  - A package cannot be installed until all its dependencies are installed
  - If any circular dependency exists, no valid installation order is possible
"""
