admins={"Dedan","Chakin"}
editors={"Chakin","Adam"}

all_users=admins.union(editors)
print("All users",all_users)
#output will be dedan,adam,chakin. Union registers everyone without repeating anybody

#who is both an editor and admiin
both_roles=admins.intersection(editors)
print("Users with both roles:",both_roles)
#intersection is a set of all members in both sets

#who is an admin only
admin_only=admins.difference(editors)
print("admin only is:",admin_only)