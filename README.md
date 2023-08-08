# Skin-Factor
This .exe app will help petroleum engineers to find all sorts of skin factors of oil wells using the correlations available.

## Overview of the app

Here is an overview of the app:

![Screenshot 2023-08-08 235501](https://github.com/Ho139523/Skin-Factor/assets/99872823/8f7c6fb7-f7df-498d-bb4c-eb0aa9c61c8e)


you can see that all this app does is to take some parameters and return a calculated value. All you need to know about the
calculation which is coded in the form of a module or library in the skin.py file is explained below:

## Using Keyboard keys in the app

If you hit enter it will return the calculation result at the bottom of the page.
And right and left keys will help you toggle between the pages.
finally, the Escape key on the last page reset all the default values shown in the entry boxes.

## Background Music

This app plays music in the background using pygame module which can be paused using the space key on the keyboard.

## Default Value

This app is designed in a way that if you enter a parameter (say, well radius) one time, it will be saved and shown 
by default value on the other pages taking that parameter again.

## Result Page

Here is an overview of the result page where you can see the total skin factor:

![Screenshot 2023-08-09 000912](https://github.com/Ho139523/Skin-Factor/assets/99872823/1b78b09a-61c1-42be-b1c9-da719ec4ff6a)


## Files and Directories

the project final .exe file is in the main root. while the codes are embedded in the skin_factor folder inside which you can
see statics folder GUI.py and skin.py. The statics folder is for all images, music,s or database files that are being used in the coding files.
GUI.py is the code related to the graphic user interface for which we've used the following libraries:

1. tkinter (design of  the app)
2. time (to do some actions with a delay of time)
3. pillow (to show images on the screen)
4. ttkbootstrap (for more advanced design)
5. pygame (to add music)
6. os and sys (to access static file directory not only from my local device but all devices that have .exe files)
7. pyautogui (to set the desired size for the app for different monitor display sizes)
8. auto-py-to-exe (to convert .py file to .exe)

## Calcuations

In Order to find the near wellbore pressure from the well-flowing rate or vice versa, petroleum engineers use Darcy equation 
inside which we see a parameter called skin factor (denoted by S). According to the Equation below:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/2ebe9793-8102-4b92-bab9-77fd1dbefd38)

Or in other words:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/c82f6265-2509-46d8-9173-7f57c3029747)


for which q stands for oil flow rate, Pr is reservoir pressure, k is permeability, h is the pay-zone thickness, μ is the fluid
viscosity, Bo is the oil formation volume factor, re is the reservoir boundary radius and rw is the well radius.

Positive skin factor is a number that causes a lower flow rate with the same pressure difference between near wellbore and 
reservoir boundary. many things can cause positive skin factor, like small tubing radius, bad perforation, and so on and so forth.

In other words, anything that blocks the fluid flow toward the well or inside the well or makes the fluid pass longer path to reach
the well is known as positive skin factor.

On the other hand, anything that helps the fluid to flow easier in the formation or inside the well is known as negative skin factor.
Like, deviation in the well trajectory, Perforation job, fracturing and etc.

There have been many scientists working on extending correlations to find this factor. I've built an .exe app to conduct the calculations
in a fraction of a second based on these correlations. I've listed them below:

## 1. Perforation skin:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/27756b3e-b287-4768-b2bb-2692a8d3f963)


![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/38b37ff9-7404-4d7a-8c8b-8cd3c36a245b)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/7f7d01c1-49c6-41db-8be4-8fd90344e5bb)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/a46351a6-5a1b-4e5b-ab5b-65d5dbdbb654)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/68b4a294-1143-45bb-b094-1c959e3155b9)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/47d0870a-34f0-4739-bcf6-de50260fcc90)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/068c9ec4-56b3-4a9d-823e-27c1981b25db)





with the constants listed in the following table:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/5152c317-6850-4d84-9aba-917df86ab10c)



## 2. Gravel-Pack skin:

(Furui)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/6d091e76-00c0-4e9e-9891-d1b7a71b207f)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/4c6afa7c-af4b-4ca2-a93e-132209714764)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/357d3b40-d14a-44a4-bd07-31dfe9bfdf56)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/97d36f1c-8cc5-4340-823c-150b4a0f015c)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/1e21dd21-528a-4761-ad4c-afd9ea7ad0be)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/1a2d5bee-476d-4f8c-8c8f-d302610cabd1)

where,

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/21163fa3-80d7-4fd6-9696-960d4c81d7df)


(Golan)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/c8875d7f-363e-4677-a669-b77841dd5741)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/5f397d32-56ef-4267-8ca8-2869e09009df)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/f0bb0486-47c6-48ee-a967-0b7945cc7265)



## 3. Slanted-Well skin:

(Cinco)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/ef62cb0d-067c-4a47-8b0a-a3f5b24e11ba)


(Besson)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/408cb105-19fa-4662-8dfa-821d97cdf4ac)


## 4. Partial-Penetration skin:

(Muskat top)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/a190e6ec-f045-4767-8f44-c98418f6402d)

(Muskat middle)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/c8bc2c16-5faa-4b8f-9303-e5422e16dcef)


(Odeh)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/71b8b4b5-fe14-4024-a527-59e71fc00153)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/7aed9c0f-f24d-41ae-864e-b05b58519e58)


(Papatzacos)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/049ab1ee-bcc1-408c-ae7a-e9bf3dbffb91)


where:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/82951593-b7b9-423b-9f73-b5747a06f19e)


##5. Non-Darcy skin:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/600362b8-e178-4fd6-8ed8-73972e4c6e25)

(Oil well)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/eb015bb8-bc74-4b2d-afe1-125ef062592f)

(Gas well)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/c4665020-3a00-4083-b289-82fd500f7515)

(Open hole)

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/a6206ce6-cc7c-49d4-96f8-8d42d4ff9a3e)


and finally one can have the total skin factor which can be used in the Darcy equation (or IPR equation)
summing up all these skins like the following:

![image](https://github.com/Ho139523/Skin-Factor/assets/99872823/0696e269-b0a2-44b0-a284-aad4a70c90df)




