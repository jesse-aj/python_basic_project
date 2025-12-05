# Unordered . Key -- value
# Also mutable

database_config = {
    "name": "alx cohort",
    "password": "secretdfbe",
    "host": "https//:aws.com"
}



print(database_config)

database_config.update({"host": "digitalocean.com"})

print(database_config)
