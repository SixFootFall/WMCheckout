# WMCheckout
Checkout system using clean architecture principles

### Installation
This project is on pure python (used version 3.8.3), you dont need to install any third-party library. I tried to create this as pure(clean) as possible :)

### Testing
To run tests you can run the command from root folder `python -m unittest discover -s ./ca -p "test*.py"`

### About this project
This is test project for Wunder Mobility assessment.

Task:"Implement a checkout system that can scan items in any order and apply certain promotional campaigns to give discounts. The system needs to be flexible regarding the promotional rules."

This is my first implementation of Clean Architecture priciples, not gonna lie, it was pretty fun! :)

All code can be (and should) well and easy tested! Any repository can be replaced with minimum effort. I loved it!

Unfortunately i didnt implement BDD here, due to lack of time.

## Infrastructure
For this task i used `MemoryRepository` without any databases and file storages.

But with help of clean architecture we can extend it and use some sort of persistance storage just by implementing 1 or 2 classes!

## Entities
### Product
To create product, use `CreateProductUseCase`.
Parameters:
  * code : str
  * name : str
  * price : positive float

Field `code` is unique in product repository. 

### Promotional Rule
To create promotional rule use `CreatePromotionalRuleUseCase`
Parameters:
  * name : str
  * discount_type : TOTAL or PRODUCT 
  * product: Product entity or None
  * target_quantity : positive int
  * measure : PERCENTAGE or CURRENCY
  * discount_amount : positive float

>Explanation:

  >**Name** - used just for orientation in rules.
  
  >**discount_type** - Can be only *TOTAL* or *PRODUCT* based. Rules with discount type *PRODUCT* is used for each product in checkout cart. Rule with type *TOTAL* will be applied after all prices in cart will be counted.
  
  >**product** - Product for PRODUCT based rules. Required if **discount_type** is *PRODUCT*.
  
  >**target_quantity** - Target for the rule. If discount type is *TOTAL* then target_quantiti is total sum. if type is *PRODUCT* - target is product quantity in Checkout cart. *i couldnt come up with better name, sorry*
  
  >**measure** - Can be only *PERCENTAGE* or *CURRENCY*.
  
  >**discount_amount** - Amount of discount. If measure is *PERCENTAGE* will be substracted *discount_amount* percentages. If measure is *CURRENCY* will be substracted *discount_amount* in currency (euros).
  
  
Examples:

To create rule like "If you spend over €30, you get 10% off your purchase" we should pass next parameters:
  * **name**="If you spend over €30, you get 10 percent off your purchase."
  * **discount_type**="TOTAL"
  * **product**=None
  * **target_quantity**=30
  * **measure**="PERCENTAGE"
  * **discount_amount**=10
 
> **target_quantity** is 30, because we are looking for *€30 spend*!
> **discount_amount** is 10, beacause we are getting 10% off total sum in cart.
  
To create rule like "If you buy 2 or more pizzas, the price for each drops to €3.99." we should pass next parameters:
  * **name**="If you buy 2 or more pizzas, the price for each drops to €3.99."
  * **discount_type**="PRODUCT"
  * **product**=<Product instance of pizza>
  * **target_quantity**=2
  * **measure**="CURRENCY"
  * **discount_amount**=2
  
> **target_quantity** is 2, because we are looking for *2 or more* pizzas in cart!
> **discount_amount** is 2, beacause base price of Pizza is 5.99, and to get 3.99 price we should substract 2 euros in currency
  
Fields (`discount_type`,`product`,`target_quantity`) is unique in promotional rules repository.

### Checkout
To implement example from task use `ExampleCheckoutUseCase`
On creating instance of `ExampleCheckoutUseCase` MemoryRepository is populating with 3 products `Curry Sauce`, `Pizza`, `Men's T-Shirt`, 2 Rules, for total and pizza product. 
Attributes:
**cart** - dict. Key of dict is Product, value of dict is product quantity in cart. Hashmap is better to find and implement quantity rules for product.

## Validation
At first i implemented unique validation in repository layer, but then i transfer it to use_cases, because uniqueness is business driven.
All entity validation (for example: "Price can be only positive") implemented in Entity layer.
But in example with price, it is better to create base class "Money" or some sort of it.
