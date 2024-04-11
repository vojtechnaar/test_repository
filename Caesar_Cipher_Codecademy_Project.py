msg = """You and your pen pal, Vishal, have been exchanging letters for some time now. Recently, he has become interested in cryptography and the two of you have started sending encoded messages within your letters.

In this project, you will use your Python skills to decipher the messages you receive and to encode your own responses! Put your programming skills to the test with these fun cryptography puzzles. Here is his most recent letter:

    Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

    For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
    
        xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
    
    This message has an offset of 10. Can you decode it?"""
    
msg = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

decode = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

msg_numbers = []

shift = 10

for sign in msg:
    if sign == " ":
       msg_numbers.append(" ")
    elif sign == "!":   
        msg_numbers.append("!")
    elif sign == "?":
       msg_numbers.append("?")
    elif sign == ".":
       msg_numbers.append(".")
    else:
        msg_numbers.append(decode.get(sign))

#print(msg_numbers)

new_msg_numbers=[]

for i in msg_numbers:
    if type(i) == type(1):
        if i+shift < 26:
            new_msg_numbers.append(i+shift)
        else:
            new_msg_numbers.append(i-26+shift)
    else:
        new_msg_numbers.append(i)

#print(new_msg_numbers)

final_msg = []

for n in new_msg_numbers:
    if type(n) == type (1):
        for key, value in decode.items():
            if value == n:
                final_msg.append(key)
    else:
        final_msg.append(n)

#print(final_msg)

final_string = "".join(final_msg)

print(final_string)

