"""
Problem 9-5 of Python Crash Course
"""
import loginAttempts2 as lA2


if __name__ == '__main__':
    me = lA2.User('tyler', 'henson', '27', 'm')
    me.greet_user()
    me.describe_user()

    for _ in range(0, 100):
        me.increment_login_attempts()
    print(me.login_attempts)

    me.reset_login_attempts()
    me.increment_login_attempts()
    print(me.login_attempts)

    me.reset_login_attempts()
    print(me.login_attempts)

    print()
    him = lA2.User('anthony', 'm', '27', 'm')
    him.greet_user()
    him.describe_user()
