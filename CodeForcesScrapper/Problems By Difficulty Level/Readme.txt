
********************************************************************************************************************************************************************
First of all make sure that chromedriver.exe is present in the directory of the script file.
********************************************************************************************************************************************************************
How to use?

Open your terminal
Check that the current working directory should be of this folder only
Fill all the required input fields

Steps:

1.Fill Minimum Difficulty of Problems and hit Enter (fill only when prompted)
2.Fill Maximum Difficulty of Problems and hit Enter (fill only when prompted)
3.Fill in the number of problems you wish to get (please note this number should be <45 else the program crashes)

Wait for the browser window to close

After this open the directory of the program and there you will find a folder with all the problems.

*********************************************************************************************************************************************************************

How does the progrm work?

after we get the number of problems, min difficulty, max difficulty
we take our driver to the page where problems with required difficulty levels are displayed
after this we iterate over the problem codes
we open the problem code links
create new directory with problem code and change cwd to the problem codes directory
(for working with directories we have imported the os module which gives us the ability to perform operations of command line using python)
take screenshot
save it in the problem code directory

afer this we note the inputs save the text in an array as string and write all of them in a text file.
same process is done for noting down outputs.
after this return to the previous webpage

now we repeat the above process number of problems times.

Finally we close the driver

***********************************************************************************************************************************************************************
