# Fun UK Lotto Number Generator.py
Using most frequently occuring numbers since the lotterys inception in the UK, this Python program generates random numbers for placing on the lotto. It also uses PyGame to add a fun visual and audio immersive element to the experience with the use of a Zoltar wish granting machine. Static Zoltar image was generated using AI prompt engineering on MidJourney.

# Table of Contents
1.	PROJECT DESCRIPTION
2.	ZOLATAR LOTTO NUMBER GENERATOR SCREENSHOT
3.	BACKGROUND
4.	TECHNOLOGIES USED
5.	REQUIREMENTS
6.	USAGE INSTRUCTIONS

# PROJECT DESCRIPTION
Using most frequently occurring numbers since the lottery’s inception in the UK, this Python program generates the most frequently drawn random numbers, for placing on the lotto. It also uses PyGame to add a fun visual and audio immersive element to the experience with the use of a Zoltar wish granting machine. Static Zoltar image was generated using AI prompt engineering on MidJourney.
# ZOLATAR LOTTO NUMBER GENERATOR SCREENSHOT
![image](https://github.com/user-attachments/assets/f6a09395-b816-49d0-9e36-d88937ec1719)

# BACKGROUND
Just like everyone else in the world I have always wished I could just win the lottery and knock the old 9-5 lifestyle on the head once and for all. No matter how many times I put money on, I rarely won a penny. In fact the most has been about £15! Not much of a life change, lucky if it would even cover a takeaway for one! I always wanted to create something to even my odds or at least give me more of chance to actually win bigger. 
<br><br>
I noticed that certain numbers like 10, came up quite regularly. So I looked into past results of the lottery which can be found online. To my surprise there are records going back to the UK lottery’s start back in the 1990’s. From this data I was able to isolate those numbers that have come up in results 10 or more times. This narrows the numbers down to a pool of 15-20 numbers that come up most frequently out of the possible 60 numbers that are possible. 
<br><br>
Although the odds are still stacked against you with these numbers, these numbers are likely to give you the greatest chance of a win. Bearing this in mind I set out to create a program to randomly select from the narrower pool of possibilities. Initially I had it generating the numbers in the console, but I really wanted to turn it into a fun experience. Which is where I thought of using Zoltar the wish granting arcade machine from the movie ‘Big’. Although I could have used an image from some free source online, I decided to use my skills in AI prompt engineering to create the image instead. This gave it a fun backdrop. But I wanted to give the whole experience more atmosphere, so I added some fairground background noise sourced online and loud mysterious laugh for when the balls were drawn. 
<br><br>
There was still something missing, Zoltar needed to speak as an intro. Turning to my AI prompt engineering once again I used an online voice generator and found a deep voice on an AI voice generator and made it say the phrase ‘Are You Feeling Lucky?’ Followed by the deep mysterious laugh. Hey presto the Fun UK Lotto Generator was born. 
<br><br>
I then spent each week testing the accuracy of the numbers. In short there was always at least 1 number that came up in the draw, but for the moment at least no BIG win…. YET!! 
<br><br>
Now it’s time to take it to the next stage and have it generate the most frequently occurring that have been shown to more likely appear together on the same lotto draw. If you have any lotto luck using it, let me know.


# TECHNOLOGIES USED
Python Packages:
1.	pygame
2.	sys
3.	random
4.	time
5.	math
   
Other Software:
1.	MidJourney AI Image Generator
2.	ElevenLabs AI Voice Synthesiser
   
# REQUIREMENTS
Python 3.11

# USAGE INSTRUCTIONS
1.	Download zoltarlotto folder and contents.
2.	From within your chosen Python code compiler (ie. VisualStudio or PyCharm), open and run the Zoltar1.py file contained in the zoltarlotto folder.
3.	The program will automatically load and generate the first set of numbers.
4.	Once you have a first set of numbers you will be prompted to run the numbers again by pressing ‘Y’ to generate more numbers, or to quit the program by pressing ‘N’.

