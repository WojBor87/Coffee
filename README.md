# **Coffee Machine Program Requirements**

### **1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”**
<ul>
    <li>Check the user’s input to decide what to do next.</li>
    <li>The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.</li>
</ul>

### **2. Turn off the Coffee Machine by entering “off” to the prompt.**
<ul>
    <li>For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.</li>
</ul>

### **3. Print report.**
<ul>
    <li>
    When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
    <ul>
        <li>Water: 100ml</li>
        <li>Milk: 50ml</li>
        <li>Coffee: 76g</li>
        <li>Money: $2.5</li>
    </ul>
    </li>
</ul>

### **4. Check resources sufficient?**
<ul>
    <li>When the user chooses a drink, the program should check if there are enough resources to make that drink.</li>
    <li>E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”</li>
    <li>The same should happen if another resource is depleted, e.g. milk or coffee.</li>
</ul>

### **5. Process coins.**
<ul>
    <li>If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.</li>
    <li>Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01</li>
    <li>Calculate the monetary value of the coins inserted.<br> E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52</li>
</ul>

### **7. Check transaction successful?**
<ul>
    <li>Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.</li>
    <li>But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.<br>
        <ul>
            <li>Water: 100ml</li>
            <li>Milk: 50ml</li>
            <li>Coffee: 76g</li>
            <li>Money: $2.5</li>
        </ul>
    </li>
  <li>If the user has inserted too much money, the machine should offer change.<br>
    E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.</li>
</ul>

### **8. Make Coffee.**
<ul>
    <li>If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.<br>
        E.g. report before purchasing latte:
        <ul>      
            <li>Water: 300ml</li>
            <li>Milk: 200ml</li>
            <li>Coffee: 100g</li>
            <li>Money: $0</li>
        </ul>  
        Report after purchasing latte:
        <ul>
            <li>Water: 100ml</li>
            <li>Milk: 50ml</li>
            <li>Coffee: 76g</li>
            <li>Money: $2.5</li>
        </ul>
    </li>
    <li>Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.</li>
</ul>