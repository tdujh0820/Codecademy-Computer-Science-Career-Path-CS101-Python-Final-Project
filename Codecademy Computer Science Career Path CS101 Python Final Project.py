import time
import random
import sys

first_loop = 0
first_sub_loop = 0
second_sub_loop = 0
number = random.randint(1, 5)
tries = 0
left = 4
temp = 0
second_loop = 0
userinformation_loop = 0
login_left = 6
correct = False
new_account = 0
overlap = True
correctlogin = 0

username_password = {}

letters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f",
           "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "!", "@", "#", "$", "%", "^", "&", "*"]
password_list = []

def type_for_each_letter(times):
    for element in times:
        print(element, end=' ')
        time.sleep(0.1)


def loading_period():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")

def line():
    time.sleep(1)
    for a in range(65):
        print("-", end="")
        time.sleep(0.05)
    print("-")
    time.sleep(0.05)


def blinking(word, space):
    n = 0
    while n < 3:
        sys.stdout.write(word)
        time.sleep(0.5)
        sys.stdout.write('\r')
        sys.stdout.write(space)
        time.sleep(0.5)
        sys.stdout.write('\r')
        n += 1


def usernamepassword():
    global userinformation_loop
    global login_left
    global correct
    global new_account
    global overlap
    global correctlogin

    for x in range(5):

        time.sleep(0.5)

        while userinformation_loop == 0:
            username_and_password = input("\033[37mDo you have your ID and your password?(y/n)\n")

            if username_and_password.lower() == "y":
                time.sleep(0.5)
                username = input("\033[37mUsername: ")
                time.sleep(0.5)
                password = input("\033[37mPassword: ")
                time.sleep(1)

                for id, pw in username_password.items():

                    if username == id and password == pw:
                        print(f"\033[37mWelcome {username}!")
                        userinformation_loop = 1
                        correctlogin = 1
                        return

                    if correctlogin == 0:
                        if login_left > 0:

                            login_left -= 1
                            print(f"\033[31mWrong username or password. ({login_left} times remaining)")
                            time.sleep(1)
                            login_again = input("\033[31mWant to try again?(y/n/press f if you forgot your password)\n")

                            if login_again.lower() == "y":
                                continue

                            elif login_again.lower() == "n":
                                time.sleep(0.5)
                                print("\033[37mBye!")
                                exit()

                            elif login_again.lower() == "f":
                                time.sleep(1)
                                find_id = input("\033[37mWhat is your id?\n")

                                for USERNAME, PASSWORD in username_password.items():
                                    if find_id == USERNAME:
                                        time.sleep(1)
                                        new_pw = input("\033[37mYour new password: ")
                                        username_password[USERNAME] = new_pw
                                        blinking("loading", "       ")
                                        blinking("loading.", "        ")
                                        blinking("loading..", "         ")
                                        blinking("loading...", "          ")
                                        time.sleep(0.5)
                                        print("\033[37mSuccessfully updated your password! Please login again")

                                    else:
                                        time.sleep(1)
                                        print("\033[31mNot existing ID. Please try again")

                            else:
                                print("\033[31mPlease write the letter 'y' or 'n'")
                                exit()

                        else:
                            print("\033[31mWrong username or password")
                            time.sleep(0.5)
                            print("\033[31mYou had lost all your 5 chances. Bye")
                            exit()

            elif username_and_password.lower() == "n":
                time.sleep(0.5)
                making_idpw = input("\033[37mDo you want to create your account?(y/n)\n")

                if making_idpw.lower() == "y":

                    while new_account == 0:
                        time.sleep(1)
                        new_id = input("\033[37mYour new username: ")
                        time.sleep(0.5)
                        new_pw = input("\033[37mYour new password: ")
                        time.sleep(2)

                        for ID, PW in username_password.items():

                            if ID == new_id:
                                print(f"\033[31mThere is already existing ID of '{new_id}'! Please try again")
                                overlap = False
                        if overlap == True:
                            break
                        else:
                            pass

                    username_password[new_id] = new_pw
                    blinking("loading", "       ")
                    blinking("loading.", "        ")
                    blinking("loading..", "         ")
                    blinking("loading...", "          ")

                    time.sleep(0.5)
                    print("\033[37mYou had successfully made your new account!")
                    time.sleep(0.5)

                    loading_period()
                    line()

                elif making_idpw.lower() == "n":
                    print("Okay, I hope you could make your account later!")
                    exit()

                else:
                    print("\033[31mPlease write the letter 'y' of 'n'")
                    exit()

            else:
                print("\033[31mPlease write the letter 'y' or 'n'")


first_choice = input("\033[32m" + "Press enter to start a game or press 'n' to quit: ")

while first_loop == 0:

    if first_choice == "":
        first_loop = 1
        usernamepassword()

    elif first_choice.lower() == "n":

        while first_sub_loop == 0:
            re_choice = input("\033[31mAre you sure? (y/n)\n")

            if re_choice == "n":
                print("\033[32mNice! you could continue the game again")
                first_sub_loop = 1
                continue

            elif re_choice == "y":
                print("\033[37mHmmm.. I hope you could play this game again. Bye!")
                exit()

            else:
                print("\033[31mPlease write letter 'y' or 'n'.")

    else:
        print("\033[31mPlease press enter or type 'n'")
        exit()

line()

time.sleep(1)
print("\033[32mLong Ago, there was a one brave warrior named '" + "\033[33mJuhwan" + "\033[32m'.")
time.sleep(3)
print("\033[32mOne day, " + "\033[33mJuhwan" + "\033[32m went for a war with the neighbor country, which had a " + "\033[31mbad king.")
time.sleep(5)
print("\033[33mJuhwan " + "\033[32mheard that the people in that country was being harmed from the " +
      "\033[31mking" + "\033[32m, so he went to that country to " + "\033[31mkill the king.")
time.sleep(5)
print("\033[32mHowever, there was a " + "\033[31mspy" + "\033[32m in Juhwan's army, and when " +
      "\033[33mJuhwan" + "\033[32m was sleeping, the " + "\033[31mspy captured him and take him to the king.")
time.sleep(5)

while second_loop == 0:
    loading_period()
    time.sleep(0.5)
    second_choice = input("\033[37mWill you go on an adventure and rescue " + "\033[33mJuhwan" + "\033[37m? (y/n)\n")

    if second_choice.lower() == "y":
        second_loop = 1
        time.sleep(0.5)
        print("Great! Good luck!")

        time.sleep(2)
        blinking("loading", "       ")
        blinking("loading.", "        ")
        blinking("loading..", "         ")
        blinking("loading...", "          ")

        time.sleep(1)
        print("\033[31mCaution!!! An enemy is ahead of you!")
        time.sleep(2)
        print("\033[31mYou need to guess the right number between 1~5! The number will be random. You have 4 chances")
        time.sleep(2)

        for i in range(4):
            guess = input("\033[37mGuess the random number from 1 to 5: ")
            time.sleep(0.5)

            try:

                if temp < 3:
                    tries += 1
                    left -= 1
                    temp += 1

                    if int(guess) == number:
                        print(f"\033[37mYou are right! You answered the question correct in {tries} time(s)")
                        time.sleep(1)
                        print("\033[32mCongratulations! You had defeated a first enemy! You could now continue the adventure!")
                        time.sleep(1)

                        i = 0

                        while i < 20:
                            sys.stdout.write('/-\\|'[i % 4])
                            time.sleep(0.5)
                            sys.stdout.write('\r')
                            i += 1

                        time.sleep(1)
                        print("\033[31mCaution!!! Another enemy is ahead of you!")
                        time.sleep(1)
                        print("\033[31mTo win this enemy, you need to solve some mathematics problems")
                        time.sleep(1)
                        print("\033[32mLet's go and beat the enemy~!")

                        line()

                        sum = input("\033[37m1. What is the sum of 987654321 + 1?\n")
                        time.sleep(0.5)

                        if int(sum) == 987654322:
                            print("\033[37mYou are correct! Moving to the next question", end="")
                            time.sleep(0.5)
                            print(".", end="")
                            time.sleep(0.5)
                            print(".", end="")
                            time.sleep(0.5)
                            print(".")

                            time.sleep(1)
                            multiplication = input("\033[37m2. What is 1 times 1?\n")
                            time.sleep(0.5)

                            if int(multiplication) == 1:
                                print("\033[37mYou are correct! Moving to the next question", end="")
                                time.sleep(0.5)
                                print(".", end="")
                                time.sleep(0.5)
                                print(".", end="")
                                time.sleep(0.5)
                                print(".")

                                time.sleep(1)
                                confused = input("\033[37m3. What is a answer of 6/2(1+2)?\n")
                                time.sleep(0.5)

                                if int(confused) == 9:
                                    print("\033[37mYou are correct!", end="")
                                    time.sleep(0.5)
                                    print(".", end="")
                                    time.sleep(0.5)
                                    print(".", end="")
                                    time.sleep(0.5)
                                    print(".")

                                    time.sleep(1)
                                    print("\033[32mCongratulations! You had defeated a second enemy!"
                                          + "You could now again continue the adventure!", end="")
                                    time.sleep(1)
                                    print("\033[32m")
                                    i = 0

                                    while i < 20:
                                        sys.stdout.write('/-\\|'[i % 4])
                                        time.sleep(0.5)
                                        sys.stdout.write('\r')
                                        i += 1

                                    time.sleep(1)
                                    print("\033[32mWow! You had now reached the king's room! You could now defeat the "
                                          + "\033[31mking" + " and rescue " + "\033[33mJuhwan!")

                                    time.sleep(2)
                                    print("\033[31mCaution!!! The king had saw you!")
                                    time.sleep(1)
                                    print("\033[31mTo win the final boss: king, you need to pick a right choice to win the king!")
                                    time.sleep(1)
                                    print("\033[32mLet's go and successfully rescue " + "\033[33mJuhwan" + "~!")

                                    line()

                                    time.sleep(0.5)
                                    print("\033[37mThe king had saw you and tries to kill you. What choice will you choose?")
                                    time.sleep(1)
                                    print("\033[34m1. Fight with him")
                                    time.sleep(0.5)
                                    print("\033[34m2. Use your invisible skill and wait until"
                                          + "the king gets tired on finding you and go outside the room")
                                    time.sleep(1)
                                    print("\033[34m3. Run away and just give up")
                                    time.sleep(0.5)
                                    print("\033[34m4. Shout out 'Juhwan is Genius!!!!!'")

                                    time.sleep(0.5)
                                    last_choice = int(input("\033[37mWhat will be your choice?(Type a number)\n"))
                                    time.sleep(1)

                                    if last_choice == 1:
                                        print("\033[31mOH NO! You died while you were fighting with the king!")
                                        print("\033[31mThe king was too powerful than you had expected")
                                        exit()

                                    elif last_choice == 2:
                                        print("\033[31mOH NO! Actually, your invisible skill only was able of 10 seconds!")
                                        exit()

                                    elif last_choice == 3:
                                        print("\033[31mOH NO! You got caught by the king!")
                                        print("\033[31mThe king was faster than you expected!!!")
                                        exit()

                                    elif last_choice == 4:
                                        print("\033[32mWow! After you had shouted that the Juhwan is Genius, the king had died!")
                                        time.sleep(1)
                                        print("\033[32mMaybe Juhwan made a spell to the king that"
                                              + "if somebody says that Juhwan is Genius, the king will die")
                                        time.sleep(2)
                                        print("\033[32mAnd congratulations! You had defeated a king of your neighbor"
                                              + "country who had taken the brave warrior Juhwan!")
                                        time.sleep(2)
                                        print("\033[32mHmm... But where is Juhwan? ")

                                        line()

                                        time.sleep(0.5)
                                        print("\033[32mLook at there! There is a hidden room that is locked with the door lock!")
                                        time.sleep(1)
                                        print("\033[37mTo unlock the room where probably Juhwan"
                                              + "is in, you need to again choose the right choice!")
                                        time.sleep(2)
                                        print("\033[34m1. Use xp to open the door")
                                        time.sleep(1)
                                        print("\033[34m2. Use your mechanic skill to reset the password")
                                        time.sleep(1)
                                        print("\033[34m3. Command other guardians of the king to open the door")
                                        time.sleep(1)
                                        print("\033[34m4. Just give up and go back to your kingdom")
                                        time.sleep(1)
                                        rescuing_choice = int(input("\033[37mWhat will be your choice?(Type a number)\n"))
                                        time.sleep(1)

                                        if rescuing_choice == 1:
                                            print("\033[31mUnfortunately, you had used all your xp on fighting with enemies")
                                            exit()

                                        elif rescuing_choice == 2:
                                            skill_yes_no = input("\033[32mGreat! Will you use your"
                                                                 + "mechanic skill to reset the password?(y/n)\n")
                                            time.sleep(1)

                                            if skill_yes_no.lower() == "y":
                                                    length = int(input("\033[37mHow long do you want your password to be? (letters)\n"))
                                                    for i in range(length):
                                                        letter = random.choice(letters)
                                                        password_list.append(letter)

                                                    password = "".join(password_list)

                                                    blinking("loading", "       ")
                                                    blinking("loading.", "        ")
                                                    blinking("loading..", "         ")
                                                    blinking("loading...", "          ")

                                                    time.sleep(1)
                                                    print(f"\033[37mThe new password is {password}!")
                                                    time.sleep(0.5)

                                                    line()

                                                    rescue = input("\033[32mWill you try to open the door of the room?(y/n)\n")
                                                    time.sleep(1)

                                                    if rescue.lower() == "y":
                                                        print("\033[32mGreat!")
                                                        time.sleep(0.5)
                                                        final_password = input("\033[37mPlease write a password for the room: ")
                                                        time.sleep(1)

                                                        if final_password == password:
                                                            print("\033[32mVaild password! Opening the door...")
                                                            time.sleep(1)
                                                            print("\033[32mWow! You found the great"
                                                                  + "brave warrior Juhwan! Congratulation!")
                                                            time.sleep(1)
                                                            exit()

                                                        elif final_password != password:
                                                            print("\033[31mInvalid password! Forbidden access")
                                                            exit()

                                                    elif rescue.lower() == "n":
                                                        print("\033[31mOkay... Good luck!")
                                                        exit()

                                                    else:
                                                        print("\033[31mPlease write the letter 'y' or 'n'")
                                                        exit()


                                            elif skill_yes_no.lower() == "n":
                                                print("\033[31mOkay... Good luck!")
                                                exit()

                                            else:
                                                print("\033[31mPlease write the letter 'y' or 'n'")
                                                exit()

                                        elif rescuing_choice == 3:
                                            print("\033[31mUnfortunately, all the guardians"
                                                  + "ran away when you defeated the king")
                                            exit()
                                        elif rescuing_choice == 4:
                                            print("\033[31mReally?? Hmm... Very disappointing...:(")
                                            exit()

                                    else:
                                        print("\033[31mYou need to write a number for the question!")
                                        exit()

                                else:
                                    print("\033[31mUnfortunately you are wrong!! The answer was 9. Hahaha~!")
                                    exit()

                            else:
                                print("\033[31mUnfortunately you are wrong!! The answer was 1. Hahaha~!")
                                exit()

                        else:
                            print("\033[31mUnfortunately you are wrong!! The answer was 987654322. Hahaha~!")
                            exit()

                    else:
                        print(f"\033[31mYou had {tries} time wrong. You got {left} times left")

                else:

                    if int(guess) == number:
                        print(f"\033[37mYou are right! You answered the question correct in {tries} time(s)")
                        print("\033[31mHowever, unfortunately, enemy had killed you"
                              + "when you were answering the question because you had used too much times!")
                        exit()

                    else:
                        print(f"\033[31mYou had used all your 3 chances! The answer was {number}! Bye~!")
                        exit()

            except ValueError:
                print("\033[31mPlease write an integer")
                exit()

    elif second_choice.lower() == "n":
        print("That's sad... Bye!")
        exit()

    else:
        print("Please write the letter 'y' or 'n'")