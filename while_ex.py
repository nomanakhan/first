# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
# print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 !=0:
#         continue
#     print(current_number)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    ch= input("Do you want to append: " )
    if ch == 'y':
        confirmed_users.append(current_user)
    else:
        continue
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())