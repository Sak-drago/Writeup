# JWT 
## *Jwt was the first problem I had solved, and was it fun learning about JSON Web Tokens!*##

### Category
**Website**

### Points
**300**

On opening the problem, we are directed to a website which says `Authentication Required`. The image has been attached below.
![image](https://github.com/Sak-drago/Writeup/assets/116898248/50a03a53-d668-433d-a9be-4cea3495ab2b)

On searching more about JWT, we find out that we can gain Authentication into the website through Cookie.
*Credit*: [Simple JWT hacking](https://medium.com/iqube-kct/simple-jwt-hacking-73870a976750)
So, we open the Inspect Tab using Inspect Element, and traverse to Storage, where we open the Cookies Tab.

![image](https://github.com/Sak-drago/Writeup/assets/116898248/d575a4d6-d60f-497a-8fa7-90438bf4c239)

From the above image, we can see that we find a cookie by the name of `jwt_session` which has the value of `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjotMX0.KYcUKjfqhf6wTJo15Bj445WkN5Y7Fr_12Vk2q-ce87c`
We also go ahead and delete the other cookie so that access is easier.

Using CyberChef, we find that the Token is encrypted in A JWT format.
![image](https://github.com/Sak-drago/Writeup/assets/116898248/9f6af665-5636-42f7-b7b0-3d3d6fe9ffb1)

Now, we have been given the hint that we have to change the value of `"user_id": -1` to `"user_id": 0`.
To do the same, we have to open a Token editor online. Surfing through the web, we find a website by name of [token.dev](https://token.dev/)

Putting the above mentioned `jwt_session` token in, we are able to see all the key details.
![image](https://github.com/Sak-drago/Writeup/assets/116898248/7006640f-e236-43d2-8306-bf9f38eb70c7)

Here, we can change the value of user_id to 0 and also change `alg` to none such that
```sh
{
  "typ": "JWT",
  "alg": "none"
}
```
Payload
```sh
{
  "user_id": 0
}
```
This gives us a new token.
*Note*: We have changed alg to none so that the signature does not get encrypted and the website takes the new token directly as we know the None Public Key.

Now, we have the new changed token with us, which is as follows `eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VyX2lkIjowfQ`
Pasting it in Storage, we get:-
![image](https://github.com/Sak-drago/Writeup/assets/116898248/dd0c5a71-2c6f-4b67-bf56-224892d58e82)

Now on reloading the page, we get the following:-
![image](https://github.com/Sak-drago/Writeup/assets/116898248/faa1829f-6c5d-4cf9-a6e0-bdd982e75835)

And BOOM! The flag is: `d4rkc0de{n0_s1gn@tur3_r3qu1r3d}`

Now we go ahead and enter the flag on the website and secure 300 Points!
