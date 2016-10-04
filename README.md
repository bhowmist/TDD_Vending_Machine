# TDD_Vending_Machine
This repository contains the scripts for test driven development of the brains of a vending machine.

Application Script - vending .py
Test Script - test.py

------------
How to run?
------------
1.Put the files in the same location ( files can be placed in differnt subfolders as well and can be called then, however for the sake of simplicity put them in the same folder).

2.Run test.py to check the test conditions.

3.To run the application in isolation with the test script, uncomment line 200-203 of the vending.py script and run vending py.

-------------------------------
How does the application work?
-------------------------------

1.First the vending machine would ask you to select an item. If you select a wrong item, that is not in the list(only items are cola,candy and chips), the machine would ask you to select the item again.

2.Then the machine would show the price to be paid and would show the insert coin option.

3.If you insert a wrong coin(only nickels, dimes and quarters are accepted), machine would ask you to insert a valid coin.

4.When you insert a valid coin, it would continue to ask for coins until the total price is paid.

5.If you change your mind and want to cancel the purchase you can press 'r'(return) button to do so. However, once the total price is paid, no return can be made.

6.Once the purcahse is done machine would display the acknowledgement and would return the change and invalid coins that you may have inserted.

7.Here, by default, the quantity for each item in the inventory is set as 10. It can be any number based on the handler of the machine. Once, for an item, the quantity in the inventory becomes 0, if you try to purcahse that item, machine would display the 'SOLD OUT' message.

8.Exact change: The machine would show 'EXACT CHANGE ONLY' when it is not able to make change with the money in it for any of the items that it sells. In the script, the minimum # for each coin is set at 2  as a condition for this operation. if there are 2 nickels, 2 dimes and 2 quarters, then we can make any amount between $0-$0.80 that is multiple of 5 and return the change. 
If quantity for any of the coins goes below 2, the machine would ask for the exact change to the customer.

---------------------------
What can be done in future?
---------------------------
This application can be improved and developed further to add more functionalities. Such as:

i. Given more than one dollar bills, you would get the option for both purchase only and change only. you would be able to get the change while not purchasing something.
