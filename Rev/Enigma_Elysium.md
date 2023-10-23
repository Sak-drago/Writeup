# Enigma Elysium
Extremely short yet fun string reading problem!

## Category
**Rev**

## Points
**200**

## Challenge Description
Oops, I forgot to uncomment the print statement

## Attached Files
[s3cr3t_k3y](https://github.com/Sak-drago/Writeup/blob/main/Rev/s3cr3t_k3y%20(1))
## Explaination
The problem has an attached file by the name of `rev_me.out`

Now, quite unfortunately, I am a windows user so .out files do not really workout for me.
On opening the file in an unreadable manner in notepad, we find see the following.
![image](https://github.com/Sak-drago/Writeup/assets/116898248/05beee17-e569-45c1-973f-69826342313b)

Now using `Ctrl+F` we open the find menu. There, we first enter `d` in the search bar and go through the code. This is beacuse we know that the flag exists in the formal of `d4rkc0de`. We come across the following.
![image](https://github.com/Sak-drago/Writeup/assets/116898248/cec542cc-47bc-45db-bc89-3a750f416fe8)

Now, since we are able to determine the flag using the flag format, the flag can be determined as `d4rkc0de{3  4_3l 1um}`.
Now, we are unaware of what `{3  4_31 1um}` means, so, we will access the same in another file type.
*Note*: We could have used Dogbolt to open the file yet we cannot since the website was not working during the RecruitmentCTF.
On accessing through MS.Doc

![image](https://github.com/Sak-drago/Writeup/assets/116898248/916fc349-1d75-435a-ac98-f3014fb1e29f)

Now we can tell that the flag is in format `d4rkc0de{3n1gm4_3ly51um}` as all the `e` are written in the form of `3`, `a` in the form `4`, `i` in the form `1`.
and thus, we have the flag

## flag
`d4rkc0de{3n1gm4_3ly51um}`
