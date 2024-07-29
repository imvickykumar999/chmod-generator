># `chmod generator`
>
>![image](https://github.com/user-attachments/assets/0c08ed0b-64c2-44b6-b581-d02572dbd645)
>![image](https://github.com/user-attachments/assets/24412b40-116d-4d87-a9b9-aa6c9d0af816)

Here are all possible cases for specifying the permissions for the owner, group, and others if you don't want the owner to have read permissions:

### Owner Permissions:
1. **No permissions:** `---`
2. **Write and execute permissions only:** `-wx`
3. **Write-only permission:** `-w-`
4. **Execute-only permission:** `--x`

### Group and Others Permissions:
For each case above, the permissions for the group and others can also be varied. Here are the possible permissions for group and others:

1. **No permissions:** `---`
2. **Read-only permission:** `r--`
3. **Write-only permission:** `-w-`
4. **Execute-only permission:** `--x`
5. **Read and write permissions:** `rw-`
6. **Read and execute permissions:** `r-x`
7. **Write and execute permissions:** `-wx`
8. **Read, write, and execute permissions:** `rwx`

### Combinations
Given the possible permissions for the owner, group, and others, you can create a variety of combinations. Here are some examples:

1. **Owner:** `---`, **Group:** `r--`, **Others:** `r--`
   ```plaintext
   chmod 044 filename
   ```
2. **Owner:** `-wx`, **Group:** `r--`, **Others:** `r--`
   ```plaintext
   chmod 371 filename
   ```
3. **Owner:** `-w-`, **Group:** `r--`, **Others:** `r--`
   ```plaintext
   chmod 241 filename
   ```
4. **Owner:** `--x`, **Group:** `r--`, **Others:** `r--`
   ```plaintext
   chmod 141 filename
   ```
5. **Owner:** `-wx`, **Group:** `r-x`, **Others:** `r-x`
   ```plaintext
   chmod 755 filename
   ```
6. **Owner:** `-w-`, **Group:** `rw-`, **Others:** `rw-`
   ```plaintext
   chmod 266 filename
   ```
7. **Owner:** `--x`, **Group:** `--x`, **Others:** `--x`
   ```plaintext
   chmod 111 filename
   ```

Here is a Python script that allows the user to specify these permissions and generate the corresponding `chmod` command:

```python
import os

def get_permission_value(permission_str):
    """Convert a permission string to its corresponding octal value."""
    permission_value = 0
    if 'r' in permission_str:
        permission_value += 4
    if 'w' in permission_str:
        permission_value += 2
    if 'x' in permission_str:
        permission_value += 1
    return permission_value

def generate_chmod_command(owner_perms, group_perms, others_perms, filename):
    """Generate the chmod command based on user input."""
    owner_value = get_permission_value(owner_perms)
    group_value = get_permission_value(group_perms)
    others_value = get_permission_value(others_perms)
    
    chmod_value = f"{owner_value}{group_value}{others_value}"
    chmod_command = f'chmod {chmod_value} "{filename}"'
    
    return chmod_command

# User input for permissions
owner_perms = input("Enter permissions for owner (e.g., ---,-wx,-w-,--x): ")
group_perms = input("Enter permissions for group (e.g., ---,-wx,r-x,rw-): ")
others_perms = input("Enter permissions for others (e.g., ---,-wx,r-x,rw-): ")
filename = input("Enter the filename: ")

# Generate chmod command
chmod_command = generate_chmod_command(owner_perms, group_perms, others_perms, filename)
print(f'The generated chmod command is: {chmod_command}')

# Execute the chmod command
os.system(chmod_command)
```

This script prompts the user to enter the desired permissions for the owner, group, and others, and then generates and executes the corresponding `chmod` command.
