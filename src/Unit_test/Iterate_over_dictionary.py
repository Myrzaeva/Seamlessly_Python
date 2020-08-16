artist = {
    "first": "Neil",
    "last": "Young",
}
# 1st way to concatenate values:
full_name = artist['first'] +" "+artist['last']
print(full_name)
# 2nd way to concatenate values:
full_name = f"{artist['first']} {artist['last']}"

# For loop with values():
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for x in donations.values():
    total_donations += x
print(total_donations)

# sum()
total_donations = sum(donations.values())

# Lambdas and sum () Built-In Functions
total_donations = sum(donation for donation
                      in donations.values())
