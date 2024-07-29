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
owner_perms = input("Enter permissions for owner (e.g., rwx, rw-, r--): ")
group_perms = input("Enter permissions for group (e.g., rwx, rw-, r--): ")
others_perms = input("Enter permissions for others (e.g., rwx, rw-, r--): ")
filename = input("Enter the filename: ")

# Generate chmod command
chmod_command = generate_chmod_command(owner_perms, group_perms, others_perms, filename)
print(f'The generated chmod command is: {chmod_command}')

# Execute the chmod command
os.system(chmod_command)

